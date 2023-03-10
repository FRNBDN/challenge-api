from rest_framework import serializers
from criteria.models import Criterion


class CriterionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    challenge = serializers.ReadOnlyField(source='challenge.title')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Criterion
        fields = [
            'id', 'owner', 'is_owner', 'challenge', 'text',
            'created_at', 'updated_at',
        ]
