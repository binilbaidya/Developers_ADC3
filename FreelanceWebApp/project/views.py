from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.db.models import Q
from django.contrib import messages
from user.forms import CreateForm
from .models import Project


# Create your views here.


















def details(request, project_id):
    template = "details.html"
    try:
        details = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist.")
    context = {
        'details': details,
        'nbar': 'project',
    }
    if request.user.is_authenticated:
        return render(request, template, context)
    else:
        return redirect('welcome')
    
def create(request):
    if request.method == "POST":
        create_form = CreateForm(request.POST)
        if create_form.is_valid():
            cform = create_form.save(commit=False)
            cform.user = request.user
            cform.save()
            messages.success(request, f'Post successfully created!')
            return redirect('project:project')
    else:
        create_form = CreateForm()
    context={
        "create_form": create_form
    }
    if request.user.is_authenticated:
        return render(request, 'create.html', context)
    else:
        return redirect('user:login')

def update(request, project_id):
    project=Project()
    project_obj = Project.objects.get(pk=project_id)
    context = {
        'project': project_obj,
    }
    uid = request.user.id
    pid = project_obj.user_id
    if uid == pid:
        return render(request, 'update.html', context)
    else:
        return redirect('project:project')

def update_db(request, project_id):
    project_obj = Project.objects.get(pk=project_id)
    project_data = request.POST
    project_obj.project_title = request.POST['title']
    project_obj.project_description = request.POST['description']
    project_obj.project_type = request.POST['pr_type']
    project_obj.save()
    messages.success(request, f'Post updated.')
    return redirect('project:project')
    
def delete(request, project_id):
    project_obj = Project.objects.get(pk = project_id)
    uid = request.user.id
    pid = project_obj.user_id
    if uid == pid:
        project_obj.delete()
        messages.success(request, f'Your post has been deleted.')
        return redirect('project:project')
    else:
        messages.warning(request, f'Cannot delete this post')
        return redirect('project:project')