from django.urls import path 
from .views import CourseCreateView , UpdateCourseView , DeleteCourseView , GetCourseView
urlpatterns = [
    
    path('create/',CourseCreateView.as_view()),
    path('update/',UpdateCourseView.as_view()),
    path('delete/',DeleteCourseView.as_view()),
    path('read/',GetCourseView.as_view()),


]