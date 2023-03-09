from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Submission
from .serializers import SubmissionSerializer
from drf_api.permission import IsOwnerOrReadOnly


class SubmissionList(APIView):
    serializer_class = SubmissionSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        submissions = Submission.objects.all()
        serializer = SubmissionSerializer(
            submissions, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        uploads = request.FILES.getlist('upload', None)
        data = {
            "title": request.POST.get('title', None),
            }
        _serializer = self.serializer_class(data=data, context={
            'uploads': uploads})
        if _serializer.is_valid():
            _serializer.save()
            return Response(data=_serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(data=_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class SubmissionDetail(APIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            submission = Submission.objects.get(pk=pk)
            self.check_object_permissions(self.request, submission)
            return submission
        except Submission.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        submission = self.get_object(pk)
        serializer = SubmissionSerializer(
            submission, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        submission = self.get_object(pk)
        serializer = SubmissionSerializer(
            submission, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        submission = self.get_object(pk)
        submission.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
