# importing required packages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm, ProfileForm, EditForm
from django.contrib import messages
from project.decorators import unauthenticated_user, authenticated_user
from django.contrib.auth.models import User
from .models import AppUser
from project.models import Project
from project.paginations import pagination

# Create your views here.
# takes required data from user and register it to database
@unauthenticated_user
def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        # check if the form is valid
        profile_form = ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            appuser = profile_form.save(commit=False)
            appuser.user = user
            appuser.save()
            username = user_form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, f'Account created successfully for { username }!')
            return redirect('project:project')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    context={
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, "user/register.html", context)

# it logouts the user and redirect to welcome page
def user_logout(request):
    logout(request)
    return redirect('message:welcome')

# it logs user in if valid
@unauthenticated_user
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are logged in as { username }!')
                return redirect('project:project')
        else:
            return render(request, 'user/login.html', context={"form": form})

    form = AuthenticationForm()
    return render(request, 'user/login.html', context={"form": form})

@authenticated_user
def view_profile(request, pk):
    detail = User.objects.get(pk=pk)
    if detail.is_superuser:
        other = None
    else:
        other = AppUser.objects.get(user_id=pk)
    object_list = Project.objects.filter(user_id=pk).order_by('-project_time')#latest projects are shown according to the latest time
    pages = pagination(request, object_list, 2)
    context = {
        "detail":detail,
        "other":other,
        'items': pages[0],
        'page_range': pages[1],
        "nbar":"profile"
    }
    return render(request,'user/view_profile.html',context)

@authenticated_user
def edit_profile(request, pk):
    post_data = request.POST or None
    file_data = request.FILES or None
    app_user = AppUser.objects.get(user=request.user)
    user_form = EditForm(post_data, instance=request.user)
    profile_form = ProfileForm(post_data,file_data, instance=app_user)
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect("user:view_profile", pk=request.user.id)

    context={
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, 'user/edit_profile.html',context)

@authenticated_user
def delete_profile(request,pk):
    main = User.objects.get(pk = pk)
    uid = request.user.id
    pid = main.id
    if uid == pid:
        main.delete()
        logout(request)
        messages.success(request, f'User has been deleted')
        return redirect('user:register')
    elif request.user.is_superuser:
        main.delete()
        messages.success(request, f'User has been deleted')
        return redirect('message:welcome')
    else:
        messages.warning(request, f'You cannot perform the following action!')
        return redirect('user:view_profile', pk = uid)

def add_funds(request):
    previous_funds = AppUser.objects.get(user=request.user).funds
    if request.method == "POST":
        funds = int(request.POST['fund'])
        funds = funds + previous_funds
        AppUser.objects.filter(user=request.user).update(funds=funds)
        return redirect('user:view_profile', pk=request.user.id)
    return render(request, "user/add_funds.html")
