from django.urls import path
from . import views

app_name = 'restapi'
urlpatterns = [
    path('projects/',views.api_data, name='api_data'),
    path('projects/<int:pk>/', views.update_api_data, name="update_data"),
]
