from rest_framework import serializers
from .models import Challenge
from criteria.models import Criteria
from submissions.models import Submission
from joins.models import Join


class ChallengeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    criteria_id = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()
    users_count = serializers.ReadOnlyField()
    submissions = serializers.SerializerMethodField()
    submissions_count = serializers.ReadOnlyField()
    completed_count = serializers.ReadOnlyField()

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

    def get_users(self, obj):
        request = self.context['request']
        joins = Join.objects.filter(
            challenge=obj
            )
        join_list = []
        for join in joins:
            join_list.append(join.member.username)
        return join_list

    def get_submissions(self, obj):
        request = self.context['request']
        submissions = Submission.objects.filter(
            challenge=obj
            )
        submissionList = []
        for submission in submissions:
            submissionList.append(submission.id)
        return submissionList

    class Meta:
        model = Challenge
        fields = [
            'id', 'owner', 'created_at', 'group', 'title',
            'date', 'is_owner', 'description', 'repetition',
            'criteria_id', 'users', 'users_count',
            'submissions', 'submissions_count', 'completed_count',
        ]
