from rest_framework import serializers
from .models import Upload
from submissions.models import Submission


class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload
        fields = [
            'id', 'submission', 'created_at', 'upload'
        ]
