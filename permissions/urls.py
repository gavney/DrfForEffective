from rest_framework.routers import DefaultRouter

from .views import (
    ResourceViewSet,
    ActionViewSet,
    PermissionViewSet,
    RoleViewSet,
    UserRoleViewSet
)

router = DefaultRouter()

router.register(
    'resources',
    ResourceViewSet
)

router.register(
    'actions',
    ActionViewSet
)

router.register(
    'permissions',
    PermissionViewSet
)

router.register(
    'roles',
    RoleViewSet
)

router.register(
    'user-roles',
    UserRoleViewSet
)

urlpatterns = router.urls