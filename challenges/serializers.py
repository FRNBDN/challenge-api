from rest_framework import serializers
from .models import Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Challenge
        fields = [
            'id', 'owner', 'created_at', 'group', 'title',
            'date', 'is_owner', 'description', 'repetition',
        ]
