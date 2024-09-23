from datetime import datetime
from django.db import models
from members.models import Member
from hashtag.models import Hashtag
# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=30)
    course_title = models.CharField(max_length=50)
    course_desc = models.TextField(max_length= 800)
    course_video_intro = models.FileField(upload_to='course/%y/%m/%d')
    course_img_video = models.ImageField(upload_to='course/images/%y/%m/%d')
    course_video_number = models.IntegerField()
    course_rating = models.IntegerField(default=0)
    course_time = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(Member , on_delete= models.CASCADE , default= 1)
    hashtags = models.ManyToManyField(Hashtag , related_name='courses')

    def rating(self):
        self.course_rating += 1
        self.save()
    