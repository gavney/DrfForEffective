from django.contrib import admin
from django.urls import include, path
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/auth/',
        include('authentication.urls')
    ),
    path(
        'api/business/',
        include('business.urls')
    ),
    path(
        '',
        HomeView.as_view(),
        name='home'
    ),
    path(
        'api/rbac/',
        include('permissions.urls')
    ),
]

