from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_amount = models.IntegerField()
    payment_details = models.TextField()
    payment_date = models.DateTimeField(auto_now_add=True)