from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.db import models
from members.models import Member
from hashtag.models import Hashtag
from django.utils.text import slugify

class ShortVideo(models.Model):
    short_title = models.CharField(max_length=100)
    short_video = models.FileField(upload_to='upload/%y/%m/%d' )
    short_likes = models.IntegerField(default= 0)
    short_comments = models.IntegerField( default=0)
    short_time = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(Member , on_delete=models.CASCADE ,default=1)
    hashtags = models.ManyToManyField(Hashtag,related_name='shortvideos',default='edify')
    slug = models.SlugField(unique= True , blank= True , max_length= 255)

    def increment_likes(self ):
        
         self.short_likes += 1
         self.save()
    def decrement_likes(self):
        if self.short_likes > 0:
            self.short_likes -= 1
            self.save()
        else:
            print("number the likes is 0 , so can't be decrease to -1")
    
    def increment_comments(self):
        self.short_comments += 1
        self.save()
    
    def decremnt_comments(self):
        if self.short_comments > 0:
            self.short_comments -=1
            self.save()
        else:
            print("number the comment is 0 , so can't be decrease to -1")
    def save(self , *args , **kwargs):
        if not self.slug:
            base_slug = slugify(self.short_title[:50])
            slug = base_slug
            num = 1
            while ShortVideo.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super(ShortVideo, self).save(*args, **kwargs)
             


    
       


    