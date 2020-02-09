from django import forms
from user.models import AppUser
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','password']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            return user

class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['phone', 'cv']

