from django.db import models

# Create your models here.

class AppUser(models.Model):
    firstname = models.CharField(max_length=100,default='test')
    lastname = models.CharField(max_length=100,default='test')
    username = models.CharField(max_length=100,default='test')
    email = models.EmailField(max_length=100,default='test@gmail.com')
    password = models.CharField(max_length=100,default='test')
    phone = models.CharField(max_length=100,default='test')
    cv = models.FileField(upload_to='cv',default='templates/base.html')
