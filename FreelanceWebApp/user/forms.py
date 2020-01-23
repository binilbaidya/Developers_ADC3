from django import forms
from user.models import AppUser
from django.contrib.auth.models import User
# from project.models import Project

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','password']
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #             user.save()
    #     return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['phone', 'cv']
# class CreateForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ('project_title', 'project_description', 'project_type')

