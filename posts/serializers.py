

from audioop import reverse
from rest_framework import serializers
from members.serializers import MemberCreateSerializer
from hashtag.models import Hashtag
from hashtag.serializers import HashtagSerializer
from .models import  Post , PostImages
import mimetypes
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from postlike.serializer import PostLikeSerializer


def validate_image_size(value: UploadedFile):
    limit_mb = 2
    print(f"Image size: {value.size} bytes, limit: {limit_mb * 1024 * 1024} bytes")  # إضافة سطر للطباعة
    if value.size > limit_mb * 1024 * 1024:
        raise ValidationError(f"حجم الصورة يجب ألا يتجاوز {limit_mb} ميجابايت.")
    return value


def validate_image_extension(value: UploadedFile):
    """
    تحقق من صحة لاحقة صورة.

    :param value: ملف الصورة المرفوع.
    :return: لا تعيد أي قيمة إذا كانت الصورة صالحة، وترفع استثناء ValidationError إذا كانت غير صالحة.
    """

    allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
    # الحصول على اللاحقة من اسم الملف وتوحيد الحروف إلى حروف صغيرة
    ext = value.name.split('.')[-1].lower()

    # التحقق من اللاحقة باستخدام قائمة الامتدادات المسموح بها
    if ext not in allowed_extensions:
        raise ValidationError("يُسمح فقط بملفات الصور (jpg, jpeg, png, gif)")

    # التحقق من نوع MIME باستخدام مكتبة mimetypes
    mime_type, _ = mimetypes.guess_type(value.name)
    if not mime_type.startswith('image/'):
        raise ValidationError("الملف المرفوع ليس صورة")

    return value

class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = [ 'id','post','member', 'image','postimage_time']
    #image = serializers.ImageField(validators=[validate_image_extension , validate_image_size])

class PostsSerializer(serializers.ModelSerializer):
    
    images = PostImagesSerializer(many = True , read_only = True)
    likes = PostLikeSerializer(many = True,read_only = True)
    comments = PostLikeSerializer(many = True,read_only = True)
    member = MemberCreateSerializer(required = False)
    slug = serializers.SlugField(required=False)
    hashtags = serializers.ListField(child = serializers.CharField(max_length = 100),write_only = True,required = False)
    share_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id','post_title','post_likes','post_comments','post_time', 'member','images','likes','comments','hashtags','slug','share_url']
     
   
    
    def create(self , validated_data):
        print(validated_data)
        hashtags_data = validated_data.pop('hashtags',None)
        post = Post.objects.create(**validated_data)
        for hashtag_name in hashtags_data:
            hashtag , created = Hashtag.objects.get_or_create(name = hashtag_name)
            post.hashtags.add(hashtag)
        return post
    def get_share_url(self, obj):
        # assuming you have a slug field, replace with ID if needed
        return f"http://127.0.0.1:8000/posts/{obj.slug}/"
        
    

    
    

    
