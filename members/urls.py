from django.urls import path
from .views import MemberCreateView, MemberDetailView, MemberListView

urlpatterns = [
    path('create/', MemberCreateView.as_view(), name='create-member'),
    path('<int:user__id>/', MemberDetailView.as_view(), name='member-detail'),  # Get member by user ID
    path('list/', MemberListView.as_view(), name='member-list'),
]
