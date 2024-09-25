from django.urls import path
from .views import CreateVideoView , UpdateVideoView , GetCourseView , DeleteCourseView
urlpatterns = [
    path("create/",CreateVideoView.as_view()),
    path("read/",GetCourseView.as_view()),
    path("update/",UpdateVideoView.as_view()),
    path("delete/",DeleteCourseView.as_view())

]