from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'project'
urlpatterns = [
    path('project/', views.project, name="project"),
    path('project/<int:project_id>', views.details, name="details"),
<<<<<<< HEAD
    url(r'^results/$', views.search, name="search"),
=======
>>>>>>> 10cee513b7c7da0c61495fc81581da8a74450a24
    path('project/create/', views.create, name = "create"),
    path('project/delete/<int:project_id>', views.delete, name="delete"),
    path('project/edit/<int:project_id>', views.update, name="update"),
    path('project/edit/update/<int:project_id>', views.update_db, name="db_update" )
<<<<<<< HEAD
=======
    
>>>>>>> 10cee513b7c7da0c61495fc81581da8a74450a24
]