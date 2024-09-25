from django.forms import ValidationError

from members.serializers import MemberCreateSerializer
from .models import Videos
from rest_framework import serializers
import mimetypes
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
import subprocess

def validate_file_size(value: UploadedFile):
    """
    يتحقق من حجم الملف، ويسمح بحد أقصى 100 ميجابايت.
    """
    max_size = 104857600  # 100 ميجابايت بالبايت
    if value.size > max_size:
        raise ValidationError("حجم الملف كبير جدًا. الحد الأقصى المسموح به هو 100 ميجابايت.")
    return value

def validate_file_extension(value: UploadedFile):
    """
    يتحقق من امتداد الملف، ويسمح فقط بملفات MP4.
    """
    allowed_extensions = ['mp4']
    ext = value.name.split('.')[-1].lower()
    mime_type, _ = mimetypes.guess_type(value.name)

    if ext not in allowed_extensions or not mime_type.startswith('video/'):
        raise ValidationError("يُسمح فقط بملفات MP4 صالحة. يرجى اختيار ملف فيديو MP4.")
    return value

class VideosSerializer(serializers.ModelSerializer):
    member = MemberCreateSerializer(required=False)
    video_video = serializers.FileField(validators=[validate_file_size, validate_file_extension ])
    class Meta:
        model = Videos
        fields = ['video_title','video_desc','video_video','video_time','course','member']
    
