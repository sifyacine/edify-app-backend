from datetime import datetime
from django.db import models
from members.models import Member
from hashtag.models import Hashtag
from django.utils.text import slugify
# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    course_desc = models.TextField(max_length= 800)
    course_video_intro = models.FileField(upload_to='course/%y/%m/%d')
    course_img_video = models.ImageField(upload_to='course/images/%y/%m/%d')
    course_video_number = models.IntegerField()
    course_rating = models.IntegerField(default=0)
    course_time = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(Member , on_delete= models.CASCADE , default= 1)
    hashtags = models.ManyToManyField(Hashtag , related_name='courses',default='edify')
    slug = models.SlugField(max_length=255,blank=True , unique=True)

    def rating(self):
        self.course_rating += 1
        self.save()
    def save(self , *args , **kwargs):
        if not self.slug:
            base_slug = slugify(self.course_title[:50])
            slug = base_slug
            num = 1
            while Courses.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super(Courses, self).save(*args, **kwargs)