from django.urls import path
from .views import GetHashtags

urlpatterns = [
    path('get/',GetHashtags.as_view())
]