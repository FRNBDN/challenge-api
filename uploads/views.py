from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Upload
from .serializers import UploadSerializer


class UploadList(generics.ListCreateAPIView):
    serializer_class = UploadSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UploadDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
