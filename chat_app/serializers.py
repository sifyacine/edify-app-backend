from rest_framework import serializers
from chat_app.models import ChatRoom, Message
from media_app.models import VideoCall
from members.models import Member


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')  # Access username from the related User model
    email = serializers.EmailField(source='user.email')  # Access email from the related User model

    class Meta:
        model = Member
        fields = ['id', 'uuid', 'username', 'email']



class ChatRoomSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)

    class Meta:
        model = ChatRoom
        fields = ['id', 'uuid', 'participants']  # Remove 'created_at'




class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'chat', 'sender', 'content', 'image', 'audio', 'video', 'created_at']



class VideoCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCall
        fields = ['id', 'chat', 'caller', 'is_active', 'created_at']
