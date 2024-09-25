from django.contrib import admin
from .models import Post, PostImages

# Inline for PostImages to show inside the Post model admin
class PostImagesInline(admin.TabularInline):
    model = PostImages
    extra = 1  # Number of empty image fields shown by default
    fields = ['image', 'postimage_time']  # Fields to display in the inline form
    readonly_fields = ['postimage_time']  # Make postimage_time readonly

# Admin model for Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_likes', 'post_comments', 'member', 'post_time')  # Fields to display in the list view
    search_fields = ('post_title', 'member__name')  # Enable search by post title or member name
    list_filter = ('post_time', 'post_likes')  # Filters to narrow down posts
    prepopulated_fields = {'slug': ('post_title',)}  # Automatically generate slug from post title
    inlines = [PostImagesInline]  # Add PostImages inline form to Post

# Admin model for PostImages
@admin.register(PostImages)
class PostImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'member', 'image', 'postimage_time')  # Fields to display in the list view
    search_fields = ('post__post_title', 'member__name')  # Enable search by post title or member name
    list_filter = ('postimage_time',)  # Filters to narrow down images
