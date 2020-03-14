from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_received')