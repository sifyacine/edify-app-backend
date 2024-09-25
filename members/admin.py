from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'joined_at', 'approved')  # Adjust fields as necessary
    search_fields = ('user__username',)  # Example of searching by username if you have a User model related to Member

# Unregister the existing Member model registration if it exists
admin.site.unregister(Member)

# Register the Member model with the custom admin class
admin.site.register(Member, MemberAdmin)
