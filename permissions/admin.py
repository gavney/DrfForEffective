from django.contrib import admin

from .models import (
    Resource,
    Action,
    Permission,
    Role,
    UserRole
)

admin.site.register(Resource)
admin.site.register(Action)
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(UserRole)