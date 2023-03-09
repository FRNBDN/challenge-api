from rest_framework import serializers
from .models import Submission, Uploads


class SubmissionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def create(self, validated_data):
        uploads = self.context['uploads']
        submission = Submission.objects.create(**validated_data)
        for upload in uploads:
            Uploads.objects.create(submission=submission, upload=upload)
        return submission

    class Meta:
        model = Submission
        fields = '__all__'
        # fields = [
        #     'id', 'owner', 'group', 'challenge', 'text',
        # ]
