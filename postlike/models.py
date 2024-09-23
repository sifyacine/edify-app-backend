from django.db import models
from members.models import Member
from posts.models import Post

from datetime import datetime
# Create your models here.
class PostLike(models.Model):
    post = models.ForeignKey(Post ,  on_delete=models.CASCADE,default=1 , related_name='likes')
    member = models.ForeignKey(Member , on_delete=models.CASCADE,default=1)
    postlike_time = models.DateTimeField(default=datetime.now())
    