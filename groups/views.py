from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Group
from .serializers import GroupSerializer
from drf_api.permissions import IsOwnerOrReadOnly

QUERYSET = Group.objects.annotate(
     members_count=Count('member', distinct=True),

    ).order_by('-created_at')


class GroupList(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = QUERYSET
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
        'tags__name',
    ]
    ordering_fields = [
        'members_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = QUERYSET
