from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.db.models import Q
from django.contrib import messages
from project.forms import Form, updateForm
from user.models import AppUser
from .models import Project, Bid
from .decorators import authenticated_user
from project.paginations import pagination

# Create your views here.

@authenticated_user   
def project(request):

    template = "project/project.html"
    object_list = Project.objects.filter(availability_status__contains=1).order_by('-project_time')#latest projects are shown according to the latest time

    pages = pagination(request, object_list, 2)

    context={
        'items': pages[0],
        'page_range': pages[1],
        'nbar': 'project',
    }
    return render(request, template, context)

# viewing the project
@authenticated_user
def details(request, project_id):#project id is passed
    template = "project/details.html"
    try:
        details = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist.")# if project doesnot exist it throws http error
    context = {
        'details': details,
        'nbar': 'project',
    }
    return render(request, template, context)

@authenticated_user
def search(request):
    template = "project/project.html"
    query = request.GET.get('q')
    if query:
        results = Project.objects.filter(Q(project_title__icontains=query) | Q(project_description__icontains=query) | Q(project_type__icontains=query))
    else:# if not authenticated he/she is redirected to welcome page
        results = Project.objects.filter(availability_status__contains=1)
    pages = pagination(request, results, 1)
    context = {
        'items': pages[0],
        'page_range': pages[1],
        'query': query,
        'nbar': 'project',
    }
    return render(request, template, context)

@authenticated_user
def create(request):
    if request.method == "POST":
        create_form = Form(request.POST)
        if create_form.is_valid():
            cform = create_form.save(commit=False)
            cform.user = request.user
            cform.save()
            messages.success(request, f'Post successfully created!')
            return redirect('project:project')
    else:
        create_form = Form()
    context={
        "create_form": create_form
    }
    return render(request, 'project/create.html', context)

# editing the existing project
@authenticated_user
def update(request, project_id):
    project_obj = Project.objects.get(pk=project_id)
    uid = request.user.id
    pid = project_obj.user_id#if user id matches with project id then update page is shown
    if uid == pid:
        post_data = request.POST or None
        uForm = updateForm(post_data, instance = project_obj) 
        if uForm.is_valid():
            uForm.save()
            messages.success(request, f'Post updated.')# message displayed by redirecting on the project page
            return redirect('project:details', project_id=project_id)
        context={
            "uForm": uForm,
        }
        return render(request, 'project/update.html', context)
    else:# else it redirects to the projects page
        messages.warning(request, f'Cannot edit this post')
        return redirect('project:project')

# Deleting a project
@authenticated_user
def delete(request,pk):# Gets id of the project to be deleted
    project_obj = Project.objects.get(pk = pk)
    uid = request.user.id
    user = request.user
    pid = project_obj.user_id
    if uid == pid or user.is_superuser:# if user id and and project id matches then the project is deleted
        project_obj.delete()
        messages.success(request, f'Post has been deleted.')
        return redirect('project:project')
    else:# message is displayed if the condition does not match
        messages.warning(request, f'Cannot delete this post')
        return redirect('project:project')

@authenticated_user
def bids(request, project_id):
    template = "project/bids.html"
    try:
        bids = Bid.objects.filter(bid_status__contains=1).order_by('-bid_time')
        project_obj = Project.objects.get(pk = project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist.")
    context = {
        'bids': bids,
        'project':project_obj,
        'nbar': 'project',
    }
    return render(request, template, context)

def add_bids(request, project_id):
    project_obj = Project.objects.get(pk = project_id)
    uid = request.user.id
    pid = project_obj.project_id
    b = Bid.objects.create(project_id=pid, user_id=uid)
    b.save()
    messages.success(request, f'You have applied for this project. Please wait while the person reviews the biddings.')
    return redirect('project:project')