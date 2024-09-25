from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from hashtag.models import Hashtag
from hashtag.serializers import HashtagSerializer
# Create your views here.
class GetHashtags(APIView):
    def post(self,request):
        try:
            hashtags = Hashtag.objects.all()
            serializer = HashtagSerializer(hashtags,many = True)
           
            return Response({"status":"success","message":serializer.data}, status=status.HTTP_200_OK)
        except Hashtag.DoesNotExist:
            return Response({"status":"failure","error":"not found"}, status=status.HTTP_404_NOT_FOUND)


