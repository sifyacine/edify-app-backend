from rest_framework import serializers
from .models import Member

# Serializer for creating a Member
class MemberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['full_name', 'general_rating', 'num_courses', 'num_reviews', 'num_followers', 
                  'is_instructor', 'about_me', 'my_posts', 'my_shorts', 'my_courses', 
                  'profile_pic', 'saved_courses', 'saved_shorts', 'saved_posts']

# Serializer for retrieving Member details
class MemberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['user', 'full_name', 'general_rating', 'num_courses', 'num_reviews', 
                  'num_followers', 'is_instructor', 'about_me', 'my_posts', 'my_shorts', 
                  'my_courses', 'profile_pic', 'saved_courses', 'saved_shorts', 'saved_posts']

# Serializer for listing Members
class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'full_name', 'general_rating', 'num_courses', 'num_reviews', 
                  'num_followers', 'is_instructor']
