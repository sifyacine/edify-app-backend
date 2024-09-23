from django.shortcuts import render
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PostComment

from posts.models import Post
from django.shortcuts import get_object_or_404
from django.db.models import F
from .serializers import PostCommentsSerializer
# Create your views here.

class CreatePostCommentView(APIView):
    def post(self, request):
        data = request.data
        serializer = PostCommentsSerializer(data = data)  
        
        try:      
                  
            if serializer.is_valid():
                serializer.save()
                post = get_object_or_404(Post , id = data['post'])
                post.post_comments = F('post_comments') +1
                post.save()
              
                return Response({'status':'success','message':serializer.data},status= status.HTTP_201_CREATED)
            return Response({'status':'failure','error':serializer.errors},status= status.HTTP_404_NOT_FOUND)
        except PostComment.DoesNotExist:
            Response({'status':'failure','error':'not exist'},status= status.HTTP_400_BAD_REQUEST)

class DeletePostCommentView(APIView):
    def post(self , request):
        data = request.data
        try:
            comment= get_object_or_404(PostComment , id = data['id'])
            post = get_object_or_404(Post , id = data['post_id'])
        except (PostComment.DoesNotExist , Post.DoesNotExist):
            return Response({'status':'failure','error':'post or comment not found'},status= status.HTTP_404_NOT_FOUND)
        comment.delete()
        post.post_comments  = F('post_comments') -1
        post.save()

     
        return Response({'status':'success'},status= status.HTTP_200_OK)
        


        

        

        