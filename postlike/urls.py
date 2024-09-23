from django.urls import path
from .views import PostLikeView

urlpatterns = [
    path('postlike/',PostLikeView.as_view())
]