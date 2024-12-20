from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import get_object_or_404
from chat_app.models import ChatRoom, Message
from chat_app.serializers import MessageSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def send_image(request, chat_uuid):
    chat = get_object_or_404(ChatRoom, uuid=chat_uuid)
    sender = request.user

    if 'image' not in request.FILES:
        return Response({'error': 'Image file is required'}, status=status.HTTP_400_BAD_REQUEST)

    image = request.FILES['image']
    group_name = f'chat_{chat_uuid}'

    message = Message.objects.create(
        chat=chat,
        sender=sender,
        image=image
    )

    # Prepare the data for real-time broadcasting
    data = {
        'id': message.id,
        'sender': sender.get_full_name(),
        'sender_short_name': sender.get_short_name(),
        'action': 'createMessage',
        'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'image': message.image.url
    }

    # Send the event to the channel layer
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name, {'type': 'send.message', 'data': data}
    )

    serializer = MessageSerializer(message)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def send_video(request, chat_uuid):
    """Send a video message to a chat room."""
    chat = get_object_or_404(ChatRoom, uuid=chat_uuid)
    sender = request.user

    if 'video' not in request.FILES:
        return Response({'error': 'Video file is required'}, status=status.HTTP_400_BAD_REQUEST)

    video = request.FILES['video']

    # Check video file size (limit: 25 MB)
    if video.size > 25 * 1024 * 1024:
        return Response({'error': 'Video file size exceeds 25 MB'}, status=status.HTTP_400_BAD_REQUEST)

    group_name = f'chat_{chat_uuid}'

    # Create a new message instance with the video
    message = Message.objects.create(
        chat=chat,
        sender=sender,
        video=video
    )

    # Prepare the data for real-time broadcasting
    data = {
        'id': message.id,
        'sender': sender.get_full_name(),
        'sender_short_name': sender.get_short_name(),
        'action': 'createMessage',
        'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'video': message.video.url
    }

    # Send the event to the channel layer
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name, {'type': 'send.message', 'data': data}
    )

    # Serialize the message and return the response
    serializer = MessageSerializer(message)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def send_audio(request, chat_uuid):
    chat = get_object_or_404(ChatRoom, uuid=chat_uuid)
    sender = request.user

    if 'audio' not in request.FILES:
        return Response({'error': 'Audio file is required'}, status=status.HTTP_400_BAD_REQUEST)

    audio = request.FILES['audio']
    audio.name = 'blob.ogg'
    group_name = f'chat_{chat_uuid}'

    message = Message.objects.create(
        chat=chat,
        sender=sender,
        audio=audio
    )

    # Prepare the data for real-time broadcasting
    data = {
        'id': message.id,
        'sender': sender.get_full_name(),
        'sender_short_name': sender.get_short_name(),
        'action': 'createMessage',
        'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'audio': message.audio.url
    }

    # Send the event to the channel layer
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name, {'type': 'send.message', 'data': data}
    )

    serializer = MessageSerializer(message)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



