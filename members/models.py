from django.db import models
from authentication.models import User  # Replace 'authentication' with the actual name of your auth app

class Member(models.Model):
    # Linking to the User model with a one-to-one relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member_profile')
    
    # Optional fields for member details
    full_name = models.CharField(max_length=255, null=True, blank=True)
    general_rating = models.FloatField(default=0.0)
    num_courses = models.PositiveIntegerField(default=0)
    num_reviews = models.PositiveIntegerField(default=0)
    num_followers = models.PositiveIntegerField(default=0)
    is_instructor = models.BooleanField(default=False)
    about_me = models.TextField(null=True, blank=True)
    
    # JSON fields for posts, shorts, and courses; allowing null and empty values by default
    my_posts = models.JSONField(default=list, null=True, blank=True)  # List of URLs for posts
    my_shorts = models.JSONField(default=list, null=True, blank=True)  # List of URLs for shorts (reels)
    my_courses = models.JSONField(default=list, null=True, blank=True)  # List of URLs for courses
    
    # Profile picture URL field
    profile_pic = models.URLField(null=True, blank=True)

    # JSON fields for saved items
    saved_courses = models.JSONField(default=list, null=True, blank=True)  # List of URLs for saved courses
    saved_shorts = models.JSONField(default=list, null=True, blank=True)  # List of URLs for saved shorts
    saved_posts = models.JSONField(default=list, null=True, blank=True)  # List of URLs for saved posts

    def __str__(self):
        return self.user.email  # Returns the email of the associated user as the string representation
