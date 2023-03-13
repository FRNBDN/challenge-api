from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Upload
from .serializers import UploadSerializer


class UploadList(APIView):
    def get(self, request):
        uploads = Upload.objects.all()
        serializer = UploadSerializer(
            uploads,
            many=True,
            context={'request': request}
            )
        return Response(serializer.data)


class UploadDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
