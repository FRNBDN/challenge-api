from rest_framework import serializers
from .models import Group
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class GroupSerializer(TaggitSerializer, serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    is_member = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    tags = TagListSerializerField()
    members = serializers.SerializerMethodField()
    members_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_is_member(self, obj):
        request = self.context['request']
        return obj.members.filter(id=request.user.id).exists()

    def get_members(self, obj):
        members = list(obj.members.all())
        membersList = []
        for member in members:
            membersList.append(member.username)
        return membersList

    class Meta:
        model = Group
        fields = [
            'id', 'owner', 'is_owner', 'is_member', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'category', 'tags', 'members', 'members_count'
        ]
