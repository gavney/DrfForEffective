from rest_framework import serializers

from .models import (
    Resource,
    Action,
    Permission,
    Role,
    UserRole
)


class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resource
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'


class UserRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRole
        fields = '__all__'