from django.urls import path
from . import views

app_name = "message"
urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('message/', views.message, name="message"),
]
