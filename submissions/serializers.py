from rest_framework import serializers
from .models import Submission
from commends.models import Commend


class SubmissionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    commend_id = serializers.SerializerMethodField()
    commends = serializers.ReadOnlyField()
    reviews = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_commend_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            commend = Commend.objects.filter(
                owner=user, submission=obj
            ).first()
            return commend.id if commend else None
        return None

    class Meta:
        model = Submission
        fields = [
            'id', 'owner', 'group', 'challenge', 'text', 'is_owner',
            'commend_id', 'commends', 'reviews',
        ]
