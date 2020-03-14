from django.shortcuts import render, redirect
from project.decorators import authenticated_user
from django.contrib.auth.models import User
from .models import Message

# Create your views here.

def welcome(request):
    return render(request, 'message/welcome.html')

#The following function helps to create a new chat room and to start a message
@authenticated_user
def new_message(request):
    Users = User.objects.all()
    return render(request, "new_message.html", context={'Users':Users, 'nbar': 'message'})

#This function is used to display the message in the chat room
@authenticated_user
def message(request, pk):
    detail = User.objects.get(pk = pk)
    message = Message.objects.all()
    return render(request, "message.html", context={'message':message, 'detail':detail, 'nbar': 'message'})

#This function is used while storing the message in the database
@authenticated_user
def create_message(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        message = request.POST['message'] #This takes the message written in the input message box
        rid = user.id #It takes the id of the user that is being watched by the current user 
        sid = request.user.id #This takes the id of the current logged in user to store in the database
        msg = Message.objects.create(message=message, receiver_id=rid, sender_id=sid)
        msg.save()
    return redirect('message:message', pk=pk)
