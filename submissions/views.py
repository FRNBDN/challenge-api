from django.db.models import Count
from rest_framework import generics, permissions
from .models import Submission
from .serializers import SubmissionSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class SubmissionList(generics.ListCreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Submission.objects.annotate(
        commends=Count(
            'commend', distinct=True
        ),
        reviews=Count(
            'review', distinct=True
        )
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SubmissionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Submission.objects.annotate(
        commends=Count(
            'commend', distinct=True
        ),
        reviews=Count(
            'review', distinct=True
        )
    )
