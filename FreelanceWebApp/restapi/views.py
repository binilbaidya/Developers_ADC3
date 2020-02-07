from django.shortcuts import render
from django.http import JsonResponse
from .models import Project
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def api_data(request):
    project = Project.objects.all()
    if request.method == "GET":
        dict_type = {"projects":list(project.values("project_title","project_description","project_status"))}
        return JsonResponse(dict_type)

# def api_data_id(request,pk):
#     project = Project.objects.get(pk=pk)
#     if request.method == "GET":
#         dict_type = {"projects":list(project.values("project_title","project_description","project_status"))}
#         return JsonResponse(dict_type)

@csrf_exempt
def update_api_data(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"project_title":project.project_title,"project_description":project.project_description,"project_status":project.project_status})
    elif request.method == "PUT":
        json_data = request.body.decode('utf-8')
        update_data = json.loads(json_data)
        project.project_title = update_data['project_title']
        project.project_description = update_data['project_description']
        project.project_status = update_data['project_status']
        project.save()
        return JsonResponse({"message":"Successfully completed!!"})
    elif request.method == "DELETE":
        project.delete()
        return JsonResponse({"message":"Successfully deleted!!"})

