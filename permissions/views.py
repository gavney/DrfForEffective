from rest_framework.viewsets import ModelViewSet

from .models import (
    Resource,
    Action,
    Permission,
    Role,
    UserRole
)

from .serializers import (
    ResourceSerializer,
    ActionSerializer,
    PermissionSerializer,
    RoleSerializer,
    UserRoleSerializer
)

from .admin_permissions import IsAdminRole


class ResourceViewSet(ModelViewSet):

    queryset = Resource.objects.all()

    serializer_class = ResourceSerializer

    permission_classes = [IsAdminRole]


class ActionViewSet(ModelViewSet):

    queryset = Action.objects.all()

    serializer_class = ActionSerializer

    permission_classes = [IsAdminRole]


class PermissionViewSet(ModelViewSet):

    queryset = Permission.objects.all()

    serializer_class = PermissionSerializer

    permission_classes = [IsAdminRole]


class RoleViewSet(ModelViewSet):

    queryset = Role.objects.all()

    serializer_class = RoleSerializer

    permission_classes = [IsAdminRole]


class UserRoleViewSet(ModelViewSet):

    queryset = UserRole.objects.all()

    serializer_class = UserRoleSerializer

    permission_classes = [IsAdminRole]