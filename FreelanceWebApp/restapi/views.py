from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Project

# Create your views here.

# This function retrieves all the data from the database
def project_data(request):
    if request.method == "GET":
        project = Project.objects.all()
        dict = {
            "projects":list(project.values("id", "project_title", "project_description", "project_type", "project_status"))
        }
        return JsonResponse(dict)

# This function returns a specific data from the database
def get_project(request, pk):
    if request.method == "GET":
        try:
            project = Project.objects.get(pk = pk)
            response = json.dumps([{'ID':project.id, 'Title':project.project_title, 'Description': project.project_description, 'Type':project.project_type, 'Status':project.project_status}])
            return HttpResponse(response, content_type='text/json')
        except:
            return JsonResponse({"Error":"No project with the given id found."})

# This functions helps to add data in Project database
@csrf_exempt
def add_project(request):
    if request.method == "POST":
        json_data = request.body.decode('utf-8')
        new = json.loads(json_data)
        project_title = new['project_title']
        project_description = new['project_description']
        project_type = new['project_type']
        project = Project.objects.create(project_title=project_title, project_description = project_description, project_type = project_type)
        try:
            project.save()
            return JsonResponse({"Success":"Project has been added successfully!"})
        except:
            return JsonResponse({"Error":"Project could not be added!"})

# This functions helps to modify or remove a data from Project database
@csrf_exempt
def update_api_data(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == "PUT":
        json_data = request.body.decode('utf-8')
        update_data = json.loads(json_data)
        project.project_title = update_data['project_title']
        project.project_description = update_data['project_description']
        project.project_type = update_data['project_type']
        project.project_status = update_data['project_status']
        project.save()
        return JsonResponse({"Success":"Project Successfully Updated!!"})
    elif request.method == "DELETE":
        project.delete()
        return JsonResponse({"Success":"Project Successfully Deleted!!"})

# Limited data shown in screen according to the size given
def project_objects_pagination(request, page_num, num_data):
	skip = num_data * (page_num - 1)
	project = Project.objects.all() [skip:(page_num*num_data)]
	dict = {
		"projects":list(project.values("id", "project_title", "project_description", "project_type", "project_status"))
	}
	return JsonResponse(dict)

