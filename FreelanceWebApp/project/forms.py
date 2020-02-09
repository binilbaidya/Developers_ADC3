from django import forms
from project.models import Project

class Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_title', 'project_description', 'project_type')

class updateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_title', 'project_description', 'project_type','project_status')