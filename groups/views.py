from django.db.models import Count
from rest_framework import generics, permissions
from .models import Group
from .serializers import GroupSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class GroupList(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Group.objects.annotate(
     members_count=Count('member', distinct=True),

    ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Group.objects.all()
