from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=100)
    project_description = models.TextField()
    availability_status = models.BooleanField(default=True)
    project_type = models.CharField(max_length=30)
    project_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_title

class Bid(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_status = models.BooleanField(default=True)
    bid_time = models.DateTimeField(auto_now_add=True)
    