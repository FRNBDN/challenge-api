from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Join
from .serializers import JoinSerializer


class JoinList(generics.ListCreateAPIView):
    serializer_class = JoinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Join.objects.all()

    def perform_create(self, serializer):
        serializer.save(member=self.request.user)


class JoinDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = JoinSerializer
    queryset = Join.objects.all()