from rest_framework import serializers
from .models import Member
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the custom user model (if using a custom one)

# Serializer for creating a Member
class MemberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            'full_name', 'general_rating', 'num_courses', 'num_reviews', 
            'num_followers', 'is_instructor', 'about_me', 'my_posts', 
            'my_shorts', 'my_courses', 'profile_pic', 'saved_courses', 
            'saved_shorts', 'saved_posts'
        ]

# Serializer for retrieving Member details (with username included)
class MemberDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)  # Include username from user model
    email = serializers.EmailField(source='user.email', read_only=True)  # Optionally include email as well

    class Meta:
        model = Member
        fields = [
            'user', 'username', 'email', 'full_name', 'general_rating', 
            'num_courses', 'num_reviews', 'num_followers', 'is_instructor', 
            'about_me', 'my_posts', 'my_shorts', 'my_courses', 'profile_pic', 
            'saved_courses', 'saved_shorts', 'saved_posts'
        ]

# Serializer for listing Members
class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            'id', 'full_name', 'general_rating', 'num_courses', 
            'num_reviews', 'num_followers', 'is_instructor'
        ]
