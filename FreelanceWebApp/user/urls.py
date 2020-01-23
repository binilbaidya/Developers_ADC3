from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
    path("view-profile/", views.view_profile, name="view_profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("delete-profile/<int:pk>/", views.delete_profile, name="delete_profile"),
]


