from django.shortcuts import render, redirect
from .models import Message

# Create your views here.

def welcome(request):
    return render(request, 'message/welcome.html')

def message(request):
    if request.user.is_authenticated:
        return render(request, "message.html", context={'nbar': 'message'})
    else:
        return redirect('message:welcome')
