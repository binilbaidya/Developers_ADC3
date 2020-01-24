from django.shortcuts import render, redirect
from .models import Message

# Create your views here.

def welcome(request):
    return render(request, 'message/welcome.html')

def message(request):
    message = Message.objects.all()
    if request.user.is_authenticated:
        return render(request, "message.html", context={'message':message, 'nbar': 'message'})
    else:
        return redirect('message:welcome')

def create_message(request):
    if request.method == "POST":
        message = request.POST['message']
        rid = 1
        sid = request.user.id
        msg = Message.objects.create(message=message, receiver_id=rid, sender_id=sid)
        msg.save()
    return redirect('message:message')
