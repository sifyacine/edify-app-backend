from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import CoursesSerializer
from rest_framework.response import Response
from .models import Courses

# Create your views here.

class CourseCreateView(APIView):
    def post(self , request):
        serializer = CoursesSerializer(data = request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetCourseView(APIView):
    def post(self,request):
        course_id = request.data.get('id')
        try:
            course = Courses.objects.get(id = course_id )
            serializer = CoursesSerializer(course)
            return Response({"status":"success","message":serializer.data},status = status.HTTP_200_OK)
        except Courses.DoesNotExist:
            return Response({"status":"failure","error":"course not found"}, status=status.HTTP_400_BAD_REQUEST)

class UpdateCourseView(APIView):
    def post(self , request):
        instance = Courses.objects.get(pk = request.data['id'])
        serializer = CoursesSerializer(instance , data = request.data,partial = True)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response({"status":"success"},status = status.HTTP_200_OK)
        return Response({"status":"failure","error":serializer.errors},status = status.HTTP_404_NOT_FOUND)

class DeleteCourseView(APIView):
    def post(self,request):
        course_id = request.data['id']
        if not course_id:
            return Response({'status':'failure','error':"id is nesscery for delete course"})
        try:    
            course = Courses.objects.get(id = course_id)
        except Courses.DoesNotExist:
            return Response({'status':'failure','error':"this course has not been founded in the database"})
        course.delete()
        return Response({'status':'success'},status=status.HTTP_200_OK)
    
class CourseDetailView(APIView):
    def get(self , request , slug , format = None):
        course = get_object_or_404(Courses , slug = slug)
        serializer = CoursesSerializer(course)
        share_url  = request.build_absolute_uri(reverse('course_detail',args = [course.slug]))
        data = serializer.data
        data['share_url'] = share_url
        return Response({'status':'success','message':data},status=status.HTTP_200_OK)

