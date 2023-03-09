from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Challenge
from .serializers import ChallengeSerializer
from drf_api.permission import IsOwnerOrReadOnly


class ChallengesList(APIView):
    serializer_class = ChallengeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        challenges = Challenge.objects.all()
        serializer = ChallengeSerializer(
            challenges, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ChallengeSerializer(
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


class ChallengeDetail(APIView):
    serializer_class = ChallengeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            challenge = Challenge.objects.get(pk=pk)
            self.check_object_permissions(self.request, challenge)
            return challenge
        except Challenge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        challenge = self.get_object(pk)
        serializer = ChallengeSerializer(
            challenge, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        challenge = self.get_object(pk)
        serializer = ChallengeSerializer(
            challenge, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        challenge = self.get_object(pk)
        challenge.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
