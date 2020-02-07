from django.shortcuts import render, redirect
from project.decorators import authenticated_user
from django.contrib.auth.models import User
from .models import Message

# Create your views here.

def welcome(request):
    return render(request, 'message/welcome.html')

@authenticated_user
def new_message(request):
    Users = User.objects.all()
    return render(request, "new_message.html", context={'Users':Users, 'nbar': 'message'})

@authenticated_user
def message(request, pk):
    detail = User.objects.get(pk = pk)
    message = Message.objects.all()
    return render(request, "message.html", context={'message':message, 'detail':detail, 'nbar': 'message'})

@authenticated_user
def create_message(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        message = request.POST['message']
        rid = user.id
        sid = request.user.id
        msg = Message.objects.create(message=message, receiver_id=rid, sender_id=sid)
        msg.save()
    return redirect('message:message', pk=pk)
