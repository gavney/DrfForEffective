from rest_framework.permissions import BasePermission

from .services import has_permission

class HasApiPermission(BasePermission):

    resource = None
    action = None

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        return has_permission(
            user=request.user,
            resource=view.resource,
            action=view.action
        )