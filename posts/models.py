from django.db import models
from datetime import datetime

from hashtag.models import Hashtag
from members.models import Member




class Post(models.Model):
    post_title = models.TextField(max_length = 800)
    post_likes = models.IntegerField(default= 0)
    post_comments = models.IntegerField(default= 0)
    post_time = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(Member , on_delete=models.CASCADE,default=1 )
    hashtags = models.ManyToManyField(Hashtag, related_name='posts')

    def __str__(self) -> str:
        return self.post_title

class PostImages(models.Model):
    post = models.ForeignKey(Post , on_delete = models.CASCADE,default=1, related_name='images')
    member = models.ForeignKey(Member , on_delete = models.CASCADE,default=1)
    image = models.ImageField(upload_to='post_images/%y/%m/%d')
    postimage_time = models.DateTimeField(auto_now_add=True)


