from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'project'
urlpatterns = [
    path('project/', views.project, name="project"),
    path('project/<int:project_id>', views.details, name="details"),
    path('project/create/', views.create, name = "create"),
    path('project/delete/<int:project_id>', views.delete, name="delete"),
    path('project/edit/<int:project_id>', views.update, name="update"),
    path('project/edit/update/<int:project_id>', views.update_db, name="db_update" )
    
]