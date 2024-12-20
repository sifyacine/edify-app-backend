from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from chat_app.models import ChatRoom, Message
from media_app.models import VideoCall
from members.models import Member
from django.shortcuts import get_object_or_404
from .serializers import ChatRoomSerializer, MessageSerializer, VideoCallSerializer, UserSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_text_message(request, chat_uuid):
    """Send a text message to a chat room."""
    chat_room = get_object_or_404(ChatRoom, uuid=chat_uuid)
    message_content = request.data.get("message", "").strip()

    if not message_content:
        return Response({"error": "Message cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)

    # Ensure the sender is a Member instance, which links to the User model
    sender = get_object_or_404(Member, user=request.user)

    # Create the message using the correct field name
    chat_message = Message.objects.create(
        chat=chat_room,
        sender=sender,
        text=message_content,  # Use 'text' as per the model definition
    )

    # Prepare the response data
    return Response({
        "id": chat_message.id,
        "chat": str(chat_message.chat.uuid),
        "sender": {
            "id": chat_message.sender.id,
            "channel_name": chat_message.sender.user.username  # Use 'username' or another field from User model
        },
        "message": chat_message.text,  # Use 'text' for returning the message content
        "created_at": chat_message.created_at.isoformat(),
    }, status=status.HTTP_201_CREATED)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_chat(request, friend_uuid):
    user = request.user
    # Fetch the Member instance for the logged-in user
    user_member = user.member_profile
    # Fetch the Member instance for the friend using the friend_uuid
    friend = get_object_or_404(Member, uuid=friend_uuid)

    # Create the chat room and add both the user and the friend as participants
    chat = ChatRoom.objects.create()
    chat.participants.add(user_member, friend)
    chat.save()

    return Response({'message': 'Chat created successfully'}, status=status.HTTP_201_CREATED)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chat_home(request):
    # Get the current user's Member instance
    member = request.user.member_profile
    
    # Filter chat rooms by the Member instance
    chats = ChatRoom.objects.filter(participants=member)
    
    # Serialize the chat rooms
    serializer = ChatRoomSerializer(chats, many=True)
    
    # Return the response
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chat_view(request, chat_uuid):
    chat = get_object_or_404(ChatRoom, uuid=chat_uuid)
    messages = Message.objects.filter(chat=chat)
    friend = Member.objects.filter(chat_rooms=chat).exclude(id=request.user.id).first()

    chat_serializer = ChatRoomSerializer(chat)
    messages_serializer = MessageSerializer(messages, many=True)
    friend_serializer = UserSerializer(friend)

    data = {
        'chat': chat_serializer.data,
        'friend': friend_serializer.data if friend else None,
        'messages': messages_serializer.data,
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_friends(request):
    user = request.user
    friends = Member.objects.filter(user__is_active=True)  # You can filter this query based on your needs
    friends_data = [{"email": friend.user.email, "uuid": friend.uuid} for friend in friends]

    return Response(friends_data, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_chatted_users(request):
    chats = ChatRoom.objects.filter(participants=request.user)
    serializer = ChatRoomSerializer(chats, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def video_view(request, chat_uuid):
    chat = get_object_or_404(ChatRoom, uuid=chat_uuid)

    call = VideoCall.objects.filter(chat=chat, is_active=True).first()
    if not call:
        call = VideoCall.objects.create(chat=chat, caller=request.user)
        call.save()

    serializer = VideoCallSerializer(call)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
