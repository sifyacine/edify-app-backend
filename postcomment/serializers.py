from rest_framework import serializers
from .models import PostComment


class PostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['post','member' , 'postcomment_content','postcomment_time']
