from django.db import IntegrityError
from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    member = serializers.ReadOnlyField(source='member.username')
    group_joined = serializers.ReadOnlyField(source='group.title')

    class Meta:
        model = Member
        fields = [
            'id', 'member', 'created_at', 'group', 'group_joined'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})