from django.urls import path
from .views import CreatePost , UpdatePost , GetPost , DeletePost ,SearchByHashtag ,PostDetailView


urlpatterns = [

    path('createpost/', CreatePost.as_view()),  
    path('getpost/', GetPost.as_view()),  
    path('updatepost/', UpdatePost.as_view()),  
    path('deletepost/', DeletePost.as_view()),  
    path('search/', SearchByHashtag.as_view()),  
    path('<slug:slug>/',PostDetailView.as_view(),name = 'post_detail')
    

    


   
]
