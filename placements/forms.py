from django import forms
from django.contrib.auth.models import User

from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['company_name', 'company_description', 'company_type', 'depts','date_of_visit','package','cgpa','contact_1','contact_2','email_id','bond','rating','website','company_logo']