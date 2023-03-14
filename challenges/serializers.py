from rest_framework import serializers
from .models import Challenge
from criteria.models import Criteria


class ChallengeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    criteria_id = serializers.SerializerMethodField()
    submissions = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_criteria_id(self, obj):
        request = self.context['request']
        criteria = Criteria.objects.filter(
            challenge=obj
            )
        criterionList = []
        for criterion in criteria:
            criterionList.append(criterion.id)
        return criterionList

    class Meta:
        model = Challenge
        fields = [
            'id', 'owner', 'created_at', 'group', 'title',
            'date', 'is_owner', 'description', 'repetition',
            'criteria_id', 'submissions',
        ]
