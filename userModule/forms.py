from django import forms
from django.contrib.auth.models import User
from .models import Role,AdminDetails
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class RoleForm(forms.ModelForm):
    type = forms.CharField()

    class Meta:
        model = Role
        fields = ['type']

class AdminForm(forms.ModelForm):

    profilepicture =forms.FileField(required=False)

    class Meta:
        model = AdminDetails
        fields = ['name','dept','rollno','gender','birthday','year','contact','profilepicture']