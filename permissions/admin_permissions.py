from rest_framework.permissions import BasePermission

from .services import has_permission


class IsAdminRole(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        return has_permission(
            user=request.user,
            resource='rbac',
            action='manage'
        )