from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Member
from .serializers import MemberSerializer


class MemberList(generics.ListCreateAPIView):
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Member.objects.all()

    def perform_create(self, serializer):
        serializer.save(member=self.request.user)


class MemberDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
