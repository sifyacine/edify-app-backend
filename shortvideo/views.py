
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShortVideoSeriliazer , LikeAndCommentSerializer 
from rest_framework.decorators import api_view
from .models import ShortVideo


class ShortVideoUploadView(APIView):
    def post(self, request):
        serializer = ShortVideoSeriliazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','message': 'تم رفع الفيديو بنجاح'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ShortVideoReadView(APIView):
    def post(self,request):
        short_id = request.data.get('id')
        try:
            shortVideo = ShortVideo.objects.get(id = short_id)
            serializer = ShortVideoSeriliazer(shortVideo)
            return Response({"status":"success","message":serializer.data} ,status=status.HTTP_200_OK)
        except ShortVideo.DoesNotExist:
            return Response({"status":"failure","error":"short video not found"}, status=status.HTTP_400_BAD_REQUEST)
            


class ShortVideoUpdateView(APIView):
    def post(self , request):
        try :
            instance = ShortVideo.objects.get(pk = request.data['id'])
            serializer = ShortVideoSeriliazer(instance , data = request.data,partial=True)
            if serializer.is_valid():
                instance.short_title = request.data["short_title"]
                instance.save()
                serializer = ShortVideoSeriliazer(instance)
                return Response({"status": "success"}, status=status.HTTP_200_OK)
            return Response({"status": "failure","error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except ShortVideo.DoesNotExist:
            return Response({"status": "failure"}, status=status.HTTP_404_NOT_FOUND)



class ShortVideoDeleteView(APIView):
    def post(self,request):
        post_id = request.data['id']
        if not post_id:
            return Response({'status':'failure','error':"id is nesscery for delete short"})
        try:    
            post = ShortVideo.objects.get(id = post_id)
        except ShortVideo.DoesNotExist:
            return Response({'status':'failure','error':"this post has not been founded in the database"})
        post.delete()
        return Response({'status':'success'},status=status.HTTP_200_OK)


        
      

class DecreseLike(APIView):
    def post(self, request):
        serializer = LikeAndCommentSerializer(data = request.data , partial = True)
        serializer.is_valid(raise_exception=True)
        video = serializer.validated_data['id']
        try:
            video_object = ShortVideo.objects.get(pk = video)
            video_object.decrement_likes()
            video_object.save()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except ShortVideo.DoesNotExist:
            return Response(
                {"status": "failure" },
                status=status.HTTP_404_NOT_FOUND,
            )


class IncreaseLike(APIView):

    def post(self, request):

        serializer = LikeAndCommentSerializer(data=request.data, partial = True)
        serializer.is_valid(raise_exception=True)

        video = serializer.validated_data['id']  # استخراج معرف الفيديو

        try:
            video_object = ShortVideo.objects.get(pk=video)
            video_object.increment_likes()
            video_object.save()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except ShortVideo.DoesNotExist:
            return Response(
                {"status": "failure"},
                status=status.HTTP_404_NOT_FOUND,
            )

    



class DecreseLike(APIView):
    def post(self, request):
        serializer = LikeAndCommentSerializer(data = request.data )
        serializer.is_valid(raise_exception=True)
        video = serializer.validated_data['id']
        try:
            video_object = ShortVideo.objects.get(pk = video, partial = True)
            video_object.decrement_likes()
            video_object.save()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except ShortVideo.DoesNotExist:
            return Response(
                {"status": "failure"},
                status=status.HTTP_404_NOT_FOUND,
            )




class IncreaseComment(APIView):
    def post(self, request):
        serializer = LikeAndCommentSerializer(data = request.data , partial = True)
        serializer.is_valid(raise_exception=True)
        video  = serializer.validated_data['id']
        try:
            video_object = ShortVideo.objects.get(pk = video)
            video_object.increment_comments()
            video_object.save()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except ShortVideo.DoesNotExist:
            return Response(
                {"status": "failure"},
                status=status.HTTP_404_NOT_FOUND,
            )


class DecreaseComment(APIView):
    def post(self, request):
        serilaizer = LikeAndCommentSerializer(data = request.data , partial = True)
        serilaizer.is_valid(raise_exception=True)
        video = serilaizer.validated_data['id']
        try:
            video_object = ShortVideo.objects.get(pk = video)
            video_object.decremnt_comments()
            video_object.save()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except ShortVideo.DoesNotExist:
            return Response(
                {"status": "failure"},
                status=status.HTTP_404_NOT_FOUND,
            )
