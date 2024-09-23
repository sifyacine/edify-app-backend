import subprocess
from django.forms import ValidationError
from rest_framework import serializers

import mimetypes
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
import subprocess

from members.serializers import MemberCreateSerializer
from hashtag.models import Hashtag
from .models import Courses

def validate_file_size(value: UploadedFile):
   
    max_size = 104857600  # 100 ميجابايت بالبايت
    if value.size > max_size:
        raise ValidationError("حجم الملف كبير جدًا. الحد الأقصى المسموح به هو 100 ميجابايت.")
    return value

def validate_file_extension(value: UploadedFile):
  
    allowed_extensions = ['mp4']
    ext = value.name.split('.')[-1].lower()
    mime_type, _ = mimetypes.guess_type(value.name)

    if ext not in allowed_extensions or not mime_type.startswith('video/'):
        raise ValidationError("يُسمح فقط بملفات MP4 صالحة. يرجى اختيار ملف فيديو MP4.")
    return value

def validate_image_size(value: UploadedFile):
    limit_mb = 2  # الحد الأقصى 2 ميجابايت
    if value.size > limit_mb * 1024 * 1024:
        raise ValidationError('يجب ألا يتجاوز حجم الصورة %s ميجابايت' % limit_mb)
    return value

def validate_image_extension(value: UploadedFile):
    allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
    ext = value.name.split('.')[-1].lower()
    mime_type, _ = mimetypes.guess_type(value.name)

    if ext not in allowed_extensions or not mime_type.startswith('image/'):
        raise ValidationError('يُسمح فقط بملفات الصور (jpg, jpeg, png, gif)')
    return value

class CoursesSerializer(serializers.ModelSerializer):
    member = MemberCreateSerializer(required = False)
    hashtags = serializers.ListField(child = serializers.CharField(max_length = 100 ),write_only = True , required = False)
    class Meta:
        model = Courses
        fields = ['course_name','course_title','course_desc','course_video_intro','course_img_video','course_video_number','course_rating','member','hashtags']
    course_video_intro = serializers.FileField(validators=[validate_file_size, validate_file_extension ])
    course_img_video = serializers.ImageField(validators=[validate_image_size , validate_image_extension ])

    def create(self , validated_data):
        hashtags_data = validated_data.pop('hashtags',None)
        course = Courses.objects.create(**validated_data)

        for hashtag_name in hashtags_data:
            hashtag , created = Hashtag.objects.get_or_create(name = hashtag_name)
            course.hashtags.add(hashtag)
        return course