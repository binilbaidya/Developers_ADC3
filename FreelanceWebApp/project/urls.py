from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'project'
urlpatterns = [
    path('project/', views.project, name="project"),
    path('project/<int:project_id>', views.details, name="details"),
    url(r'^results/$', views.search, name="search"),
    path('project/create/', views.create, name = "create"),
    path('project/delete/<int:pk>', views.delete, name="delete"),
    path('project/edit/<int:project_id>', views.update, name="update"),
    path('project/bids/<int:project_id>', views.bids, name="bids"),
    path('project/add-bids/<int:project_id>', views.add_bids, name="add_bids"),   
]