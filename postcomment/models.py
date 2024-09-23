from django.db import models
from datetime import datetime

from members.models import Member
from posts.models import Post
# Create your models here.


class PostComment(models.Model):
    post = models.ForeignKey(Post , on_delete= models.CASCADE,default= 1,related_name='comments')
    member = models.ForeignKey(Member , on_delete= models.CASCADE , default= 1)
    postcomment_content = models.CharField(max_length= 200)
    postcomment_time = models.DateTimeField(default= datetime.now())