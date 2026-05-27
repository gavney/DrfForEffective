from .models import UserRole


def has_permission(user, resource, action):

    permission_code = f'{resource}:{action}'

    user_roles = UserRole.objects.filter(
        user=user
    ).select_related('role').prefetch_related(
        'role__permissions'
    )

    for user_role in user_roles:

        role = user_role.role

        permissions = role.permissions.all()

        for permission in permissions:

            if permission.code == permission_code:
                return True

    return False