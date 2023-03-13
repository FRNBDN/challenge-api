from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Criterion
from .serializers import CriterionSerializer


class CriteriaList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Criterion.objects.all()
    serializer_class = CriterionSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CriterionDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Criterion.objects.all()
    serializer_class = CriterionSerializer
