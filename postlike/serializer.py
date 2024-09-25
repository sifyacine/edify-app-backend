from .models import PostLike
from rest_framework import serializers

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['post','member','postlike_time']