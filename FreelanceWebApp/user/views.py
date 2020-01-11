from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import Form, AppUserForm
from django.contrib import messages
from .models import AppUser
from project.views import Project 

# Create your views here.

def register(request):
    if request.method == "POST":
        form = Form(request.POST)
        appuser_form = AppUserForm(request.POST)
        if form.is_valid() and appuser_form.is_valid():
            user = form.save()
            
            appuser = appuser_form.save(commit=False)
            appuser.user = user
            
            appuser.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, f'Account created successfully for { username }!')
            return redirect('project:project')
    else:
        form = Form()
        appuser_form = AppUserForm()

    context={
        "form": form,
        "appuser_form": appuser_form
    }
    if request.user.is_authenticated:
        return redirect('project:project')
    else:
        return render(request, "register.html", context)

def user_logout(request):
    logout(request)
    return redirect('message:welcome')

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

    form = AuthenticationForm()

    if request.user.is_authenticated:
        return redirect('project:project')
    else:
        return render(request, 'login.html', context={"form": form})