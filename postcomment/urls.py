from django.urls import path
from .views import CreatePostCommentView , DeletePostCommentView
urlpatterns = [
    path('create/',CreatePostCommentView.as_view()),
    path('delete/',DeletePostCommentView.as_view()),

]