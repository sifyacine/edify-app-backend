from django.urls import path
from .views import ShortVideoUploadView , ShortVideoReadView ,ShortVideoDeleteView, IncreaseComment , DecreseLike , IncreaseLike, DecreaseComment , ShortVideoUpdateView
urlpatterns = [
    path('create/',ShortVideoUploadView.as_view()),
    path('update/',ShortVideoUpdateView.as_view()),
    path('delete/',ShortVideoDeleteView.as_view()),
    path('read/',ShortVideoReadView.as_view()),
    path('increaselike/',IncreaseLike.as_view()),
    path('decreaselike/',DecreseLike.as_view()),
    path('increasecomment/',IncreaseComment.as_view()),
    path('decreasecomment/',DecreaseComment.as_view()),
]