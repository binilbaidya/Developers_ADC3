from django.urls import path
from . import views

app_name = "message"
urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('message/', views.new_message, name="new_message"),
    path('message/<int:pk>/', views.message, name="message"),
    path('message/<int:pk>/save/',views.create_message, name="create_message"),
]
