from profile import Profile

from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import Role, Profile


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'id')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    role = RoleSerializer()
    picture = serializers.ImageField()

    class Meta:
        model = Profile
        fields = "__all__"


class PermissionSerializer(serializers.Serializer):
    type = serializers.CharField(allow_blank=False, max_length=155)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False, max_length=155)
    password = serializers.CharField(allow_blank=False, max_length=155)


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
