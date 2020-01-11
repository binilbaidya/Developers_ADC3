from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AppUser
from project.models import Project

class Form(UserCreationForm):
	first_name = forms.CharField(max_length=40)
	last_name = forms.CharField(max_length=40)
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('first_name','last_name','username', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super().save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class AppUserForm(forms.ModelForm):
	class Meta:
		model = AppUser
		fields = ('phone', 'upload_cv')

class CreateForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ('project_title', 'project_description', 'project_type')