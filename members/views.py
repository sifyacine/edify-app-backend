from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Member
from .serializers import MemberCreateSerializer, MemberDetailSerializer, MemberListSerializer

# View to create a new member
class MemberCreateView(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically associate the current user with the Member profile
        serializer.save(user=self.request.user)

# View to get details of a single member using username
class MemberDetailView(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user__username'  # Get details using the user's username

# View to list all members
class MemberListView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberListSerializer
    permission_classes = [IsAuthenticated]
