from django import forms
from user.models import AppUser
from django.contrib.auth.models import User
# from project.models import Project

class UserForm(forms.ModelForm):
    password1 = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','password1']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['phone', 'cv']

