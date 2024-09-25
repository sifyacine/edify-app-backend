from datetime import datetime
from django.db import models
from members.models import Member
from courses.models import Courses
# Create your models here.
class  Videos(models.Model):
    
    video_title = models.CharField(max_length=50)
    video_desc = models.CharField(max_length=800)
    video_video = models.FileField(upload_to= 'video/%y/%m/%d')
    video_time = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Courses , on_delete= models.CASCADE , default= 1)
    member = models.ForeignKey(Member , on_delete=models.CASCADE , default= 1)

