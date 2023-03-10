from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Commend
from .serializers import CommendSerializer


class CommendList(generics.ListCreateAPIView):
    serializer_class = CommendSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Commend.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommendDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommendSerializer
    queryset = Commend.objects.all()
