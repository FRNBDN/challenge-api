from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

QUERYSET = Profile.objects.annotate(
        groups_joined=Count('owner__group', distinct=True),
        followers_count=Count(
            'owner__followed', distinct=True
            ),
        following_count=Count(
            'owner__following', distinct=True
            ),
        challenges_created=Count(
            'owner__challenge', distinct=True
            ),
        challenges_interactions=Count(
            'owner__challenge__submission__commend', distinct=True
        )+Count(
            'owner__challenge__submission__review', distinct=True
        )+Count(
            'owner__challenge__submission', distinct=True
        )
    ).order_by('-created_at')


class ProfileList(generics.ListAPIView):
    queryset = QUERYSET
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile'
    ]
    ordering_fields = [
        'groups_joined',
        'followers_count',
        'following_count',
        'challenges_created',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]
    search_fields = [
        'owner__username',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = QUERYSET
    serializer_class = ProfileSerializer
