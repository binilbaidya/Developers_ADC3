from django.db import models

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=100)
    project_description = models.TextField()
    project_type = models.CharField(max_length=30)
    project_status = models.BooleanField(default=True)

