from django import forms
from user.models import AppUser
# from project.models import Project

class Form(forms.ModelForm):

    class Meta:
        model = AppUser
        fields = ('firstname','lastname','username','email','password','phone','cv')

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #             user.save()
    #     return user

# class CreateForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ('project_title', 'project_description', 'project_type')
