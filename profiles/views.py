from django.db.models import Count
from rest_framework import generics, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        groups_joined=Count('owner__group', distinct=True),
        followers_count=Count(
            'owner__followed', distinct=True
            ),
        following_count=Count(
            'owner__following', distinct=True
            ),
        challenges_created=Count(
            'owner__challenge', distinct=True
            )
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'groups_joined',
        'followers_count',
        'following_count',
        'challenges_created',
        'owner__following__created_at'
        'owner__followed__created_at'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        groups_joined=Count('owner__group', distinct=True),
        followers_count=Count(
            'owner__followed', distinct=True
            ),
        following_count=Count(
            'owner__following', distinct=True
            ),
        challenges_created=Count(
            'owner__challenge', distinct=True
            )
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
