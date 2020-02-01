from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.db.models import Q
from django.contrib import messages
from project.forms import Form
from user.models import AppUser
from .models import Project, Bid
from project.paginations import pagination

# Create your views here.

def project(request):

    template = "project/project.html"
    object_list = Project.objects.filter(project_status__contains=1).order_by('-project_time')#latest projects are shown according to the latest time

    pages = pagination(request, object_list, 2)

    context={
        'items': pages[0],
        'page_range': pages[1],
        'nbar': 'project',
    }
    if request.user.is_authenticated:
        return render(request, template, context)
    else:
        return redirect('message:welcome')

# viewing the project
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
    if request.user.is_authenticated:# if the user is authenticated user is redirected to project details
        return render(request, template, context)
    else:
        return redirect('welcome')

def search(request):
    template = "project/project.html"
    query = request.GET.get('q')
    if query:
        results = Project.objects.filter(Q(project_title__icontains=query) | Q(project_description__icontains=query) | Q(project_type__icontains=query))
    else:# if not authenticated he/she is redirected to welcome page
        results = Project.objects.filter(project_status__contains=1)
    pages = pagination(request, results, 1)
    context = {
        'items': pages[0],
        'page_range': pages[1],
        'query': query,
        'nbar': 'project',
    }
    if request.user.is_authenticated:
        return render(request, template, context)
    else:
        return redirect('message:welcome')

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
    if request.user.is_authenticated:
        return render(request, 'project/create.html', context)
    else:
        return redirect('user:login')

# editing the existing project
def update(request, project_id):
    project=Project()
    project_obj = Project.objects.get(pk=project_id)
    context = {
        'project': project_obj,
    }
    uid = request.user.id
    pid = project_obj.user_id#if user id matches with project id then update page is shown
    if uid == pid:
        return render(request, 'project/update.html', context)
    else:# else it stays on the current page
        return redirect('project:project')
# update database
def update_db(request, project_id):
    project_obj = Project.objects.get(pk=project_id)
    project_data = request.POST

    # Gives user the chance to update
    project_obj.project_title = request.POST['title']
    project_obj.project_description = request.POST['description']
    project_obj.project_type = request.POST['pr_type']
    project_obj.save() # changes are saved
    messages.success(request, f'Post updated.')# message displayed by redirecting on the project page
    return redirect('project:project')

# Deleting a project
def delete(request,pk):# Gets id of the project to be deleted
    project_obj = Project.objects.get(pk = pk)
    uid = request.user.id
    pid = project_obj.user_id
    if uid == pid:# if user id and and project id matches then the project is deleted
        project_obj.delete()
        messages.success(request, f'Your post has been deleted.')
        return redirect('project:project')
    else:# message is displayed if the condition does not matchs
        messages.warning(request, f'Cannot delete this post')
        return redirect('project:project')

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
    
    if request.user.is_authenticated:
        return render(request, template, context)
    else:
        return redirect('message:welcome')

def add_bids(request, project_id):
    project_obj = Project.objects.get(pk = project_id)
    uid = request.user.id
    pid = project_obj.project_id
    b = Bid.objects.create(project_id=pid, user_id=uid)
    b.save()
    messages.success(request, f'You have applied for this project. Please wait while the person reviews the biddings.')
    return redirect('project:project')