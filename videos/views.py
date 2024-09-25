from .models import Videos
from .serializers import VideosSerializer
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class CreateVideoView(APIView):
    def post(self,request):
        print(request.FILES)
        serializer = VideosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({"status":"success","message":serializer.data},status = status.HTTP_201_CREATED)
        return Response({"status":"failure","error":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
class GetCourseView(APIView):
    def post(self, request):
        course_id = request.data.get('id')
        try:
            video = Videos.objects.get(course = course_id)
            serializer = VideosSerializer(video)
            
            return Response({'status':'success','message':serializer.data},status = status.HTTP_200_OK)
        except Videos.DoesNotExist:
            return Response({'status':'failure','error':'video not found'},status = status.HTTP_200_OK)
              

class UpdateVideoView(APIView):
    def post(self , request):
        
        try:
            instance = Videos.objects.get(pk = request.data['id'])
            serializer = VideosSerializer(instance , data = request.data,partial = True)
            if serializer.is_valid():
                
                serializer.save()
                return Response({"status":"success"},status = status.HTTP_200_OK)
            return Response({"status":"failure","error":"can't update video"},status = status.HTTP_404_NOT_FOUND)
        except Videos.DoesNotExist:
            return Response({"status":"failure","error":"can't update video"},status = status.HTTP_404_NOT_FOUND)


class DeleteCourseView(APIView):
    def post(self,request):
            video_id = request.data['id']
            if not video_id:
                return Response({'status':'failure','error':"id is nesscery for delete video"})
            try:    
                course = Videos.objects.get(id = video_id)
            except Videos.DoesNotExist:
                return Response({'status':'failure','error':"this video has not been founded in the database"})
            course.delete()
            return Response({'status':'success'},status=status.HTTP_200_OK)

