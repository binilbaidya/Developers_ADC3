from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    user = models.ManyToManyField(User)
    message_title = models.CharField(max_length=40)
    message_time = models.DateTimeField(auto_now_add=True)
    message_body = models.TextField()