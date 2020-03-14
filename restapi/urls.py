from django.urls import path
from . import views

app_name = 'restapi'
urlpatterns = [
    path('projects/',views.project_data),
    path('projects/<int:pk>/',views.get_project),
    path('projects/new/', views.add_project),
    path('projects/paginated/<int:page_num>/<int:num_data>', views.project_objects_pagination),
    path('projects/change/<int:pk>/', views.update_api_data),
]
