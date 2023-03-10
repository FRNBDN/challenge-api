from django.db import IntegrityError
from rest_framework import serializers
from .models import Join


class JoinSerializer(serializers.ModelSerializer):
    member = serializers.ReadOnlyField(source='member.username')
    challenge_name = serializers.ReadOnlyField(source='challenge.title')

    class Meta:
        model = Join
        fields = [
            'id', 'member', 'created_at', 'challenge', 'challenge_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
