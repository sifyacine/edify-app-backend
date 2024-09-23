
from members.models import Member
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from posts.models import Post
from .models import PostLike

from django.db.models import F
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# ... باقي الـ imports

class PostLikeView(APIView):
    def post(self, request):
        try:
            post = get_object_or_404(Post , id = request.data['post'])
            member = get_object_or_404(Member ,id = request.data['member'])
        except (Post.DoesNotExist , Member.DoesNotExist):
            return Response({"status":"failure",'error':"channel or post are not exist"},status = status.HTTP_404_NOT_FOUND)
        post_like , created = PostLike.objects.get_or_create(post = post , channel = Member)
        if not created:
            post_like.delete()
            post.post_likes = F('post_likes') -1
            message = "unLike"
        else:
            post.post_likes = F('post_likes') +1
            message = "Like"
            post.save()
            post.refresh_from_db()
        return Response({"status":"success","message":message},status = status.HTTP_200_OK)




            