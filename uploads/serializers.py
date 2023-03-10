from rest_framework import serializers
from .models import Upload
from submissions.models import Submission


class UploadSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Upload
        fields = [
            'id', 'owner', 'is_owner', 'submission', 'created_at', 'upload'
        ]
