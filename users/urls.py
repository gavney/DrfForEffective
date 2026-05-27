from django.urls import path

from .views import ProfileUpdateView, DeleteAccountView

urlpatterns = [

    path(
        'me/update/',
        ProfileUpdateView.as_view(),
        name='profile-update'
    ),

    path(
        'me/delete/',
        DeleteAccountView.as_view(),
        name='delete-account'
    ),
]