from rest_framework import serializers
from .models import Challenge
from criteria.models import Criteria
from submissions.models import Submission
from joins.models import Join


class ChallengeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    criteria = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()
    users_count = serializers.ReadOnlyField()
    submissions = serializers.SerializerMethodField()
    submissions_count = serializers.ReadOnlyField()
    completed_count = serializers.ReadOnlyField()
    joined_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_criteria(self, obj):
        request = self.context['request']
        criteria = Criteria.objects.filter(
            challenge=obj
            )
        criterion_list = []
        for criterion in criteria:
            criterion_list.append(criterion.id)
        return criterion_list

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

    def get_joined_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            join = Join.objects.filter(
                member=user, challenge=obj
            ).first()
            return join.id if join else None
        return None

    class Meta:
        model = Challenge
        fields = [
            'id', 'owner', 'created_at', 'group', 'title',
            'date', 'is_owner', 'description', 'repetition',
            'criteria', 'users', 'users_count', 'joined_id',
            'submissions', 'submissions_count', 'completed_count',
        ]
