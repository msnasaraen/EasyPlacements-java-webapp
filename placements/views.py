# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
from .forms import CompanyForm
from .models import Company
from django.core import serializers
from .Serializers import CarSerializer
import json
# Create your views here.

def addCompany(request):
    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        return render(request,'placements/addCompany.html')

def companyDetail(request):
    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        return render(request,'placements/companyDetail.html')


def addCompanyDetails(request):
    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        form = CompanyForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print "sccess"
            company = form.save(commit=False)
            company.user = request.user
            company.company_logo = request.FILES['company_logo']
            company.save()
        return render(request, 'placements/companyDetail.html')

def getCompanies(request):
    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        company = Company.objects.all()
        #print company
        #serialized_obj = serializers.serialize("json", company)
        #print serialized_obj
        #json_data = json.loads(serialized_obj)
        #print json_data[0]

        results = [ob.as_json() for ob in company]
        print str(results)
        return JsonResponse(results,safe=False)




