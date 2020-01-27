# importing required packages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm, ProfileForm, EditForm
from django.contrib import messages
from .models import AppUser
from project.views import Project

# Create your views here.
# takes required data from user and register it to database
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
    if request.user.is_authenticated:
        return redirect('project:project')
    else:
        return render(request, "user/register.html", context)

# it logouts the user and redirect to welcome page
def user_logout(request):
    logout(request)
    return redirect('message:welcome')

# it logs user in if valid
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
            # messages.info(request, f'Invalid username or password')
            return render(request, 'user/login.html', context={"form": form})

    form = AuthenticationForm()

    if request.user.is_authenticated:
        return redirect('project:project')
    else:
        return render(request, 'user/login.html', context={"form": form})


def view_profile(request):
    other = AppUser.objects.get(user=request.user)
    context = {
        "user":request.user,
        "other":other
          }
    return render(request,'user/view_profile.html',context)
def edit_profile(request):
    post_data = request.POST or None
    file_data = request.FILES or None
    app_user = AppUser.objects.get(user=request.user)
    user_form = EditForm(post_data, instance=request.user)
    profile_form = ProfileForm(post_data,file_data, instance=app_user)
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect("user:view_profile")

    context={
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, 'user/edit_profile.html',context)

def delete_profile(request,pk):
    profile = AppUser.objects.get(pk=pk)
    profile.delete()
    logout(request)
    return redirect('user:register')


def add_funds(request):
    previous_funds = AppUser.objects.get(user=request.user).funds
    if request.method == "POST":
        funds = int(request.POST['fund'])
        funds = funds + previous_funds
        AppUser.objects.filter(user=request.user).update(funds=funds)
        return redirect('user:view_profile')
    return render(request, "user/add_funds.html")
