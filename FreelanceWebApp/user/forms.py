from django import forms
from user.models import AppUser
from django.contrib.auth.models import User
# from project.models import Project

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['phone', 'cv']

