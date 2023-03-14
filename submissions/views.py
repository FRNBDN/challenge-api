from django.db.models import Count
from rest_framework import generics, permissions
from .models import Submission
from .serializers import SubmissionSerializer
from drf_api.permissions import IsOwnerOrReadOnly

QUERYSET = Submission.objects.annotate(
        commends=Count(
            'commend', distinct=True
        ),
        reviews=Count(
            'review', distinct=True
        )
    )


class SubmissionList(generics.ListCreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = QUERYSET

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SubmissionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = QUERYSET
