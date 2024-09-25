from django.contrib import admin
from .models import Member

admin.site.register(Member)
from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    # Specify fields to display in the list view
    list_display = (
        'user',          # Display the associated User
        'full_name',     # Display the full name
        'is_instructor', # Show if the user is an instructor
        'num_courses',   # Display the number of courses
        'num_followers', # Display the number of followers
        'general_rating' # Display the general rating
    )
    
    # Add search functionality to search by user email or full name
    search_fields = ('user__email', 'full_name')
    
    # Add filters to filter members by instructor status
    list_filter = ('is_instructor',)

    # Optionally, you can add pagination if you expect many members
    list_per_page = 20  # Display 20 members per page

# Register the custom admin class
admin.site.register(Member, MemberAdmin)
