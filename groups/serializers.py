from rest_framework import serializers
from .models import Group
from members.models import Member
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class GroupSerializer(TaggitSerializer, serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    member_id = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    tags = TagListSerializerField()
    members = serializers.SerializerMethodField()
    members_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_member_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            member = Member.objects.filter(
                member=user, group=obj
            ).first()
            return member.id if member else None
        return None

    def get_members(self, obj):
        members = Member.objects.filter(
            group=obj
        )
        members_list = []
        for member in members:
            members_list.append(member.member.username)
        return members_list

    class Meta:
        model = Group
        fields = [
            'id', 'owner', 'is_owner', 'member_id', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'category', 'tags', 'members', 'members_count'
        ]
