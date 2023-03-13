from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Group
from .serializers import GroupSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class GroupList(APIView):
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(
            groups, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = GroupSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class GroupDetail(APIView):
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            group = Group.objects.get(pk=pk)
            self.check_object_permissions(self.request, group)
            return group
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        group = self.get_object(pk)
        serializer = GroupSerializer(
            group, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        group = self.get_object(pk)
        serializer = GroupSerializer(
            group, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        group = self.get_object(pk)
        group.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
