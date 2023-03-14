from django.db.models import Count, Q
from rest_framework import generics, permissions
from .models import Challenge
from .serializers import ChallengeSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class ChallengesList(generics.ListCreateAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Challenge.objects.annotate(
     users_count=Count('join', distinct=True),
     submissions_count=Count('submission', distinct=True),
     completed_count=Count(
        'submission', filter=Q(submission__status=2)
        )
    ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChallengeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Challenge.objects.all()
