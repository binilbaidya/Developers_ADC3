from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    cv = models.FileField(upload_to='cv', null=True, blank=True, default="No")
    funds = models.IntegerField(blank=True,null=True,default=0)

