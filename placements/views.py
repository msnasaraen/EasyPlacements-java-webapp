# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.db.models import F
from .forms import CompanyForm
from .models import Company
from userModule.models import Role,UserDetails,AdminDetails
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

def usercompanyDetail(request):
    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        return render(request,'placements/userCompanyDetails.html')

def approveUsers(request):
    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        return render(request,'placements/ApproveUsers.html')

def approveAdmin(request):
    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        return render(request,'placements/ApproveAdmin.html')

def getUsersForApproval(request):
    context = {"status":"failed"}

    listOfUser = Role.objects.filter(isApproved="no" ,isDetailsProvided="yes",type="user")
    print listOfUser
    results = [ob.as_jsonApproveUser() for ob in listOfUser]
    print results
    return JsonResponse(results,safe=False)

def getAdminForApproval(request):
    context = {"status":"failed"}

    listOfUser = Role.objects.filter(isApproved="no",type="admin")
    results = [ob.as_jsonApproveAdmin() for ob in listOfUser]
    print results
    return JsonResponse(results,safe=False)


def addCompanyDetails(request):
    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        data = request.POST.get('companyDetails')
        unicodedata = json.loads(data)
        form = CompanyForm(unicodedata, request.FILES or None)
        if form.is_valid():
            print "sccess"
            company = form.save(commit=False)
            company.user = request.user
            company.company_logo = request.FILES['company_logo']
            company.save()
            print "good"
        return render(request, 'placements/companyDetail.html')

def getCompanies(request):
    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        company = Company.objects.all()
        results = [ob.as_json() for ob in company]
        print str(results)
        return JsonResponse(results,safe=False)

def getCompaniesUser(request):
    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        company = Company.objects.all()
        results = [ob.as_jsonUser() for ob in company]
        print str(results)
        return JsonResponse(results,safe=False)


def getElligibleCompaniesUser(request):
    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        cgpa = UserDetails.objects.get(user = request.user).cgpa
        company = Company.objects.filter(cgpa__lte=cgpa)
        results = [ob.as_jsonUser() for ob in company]
        print str(results)
        return JsonResponse(results,safe=False)


def approvethisadmin(request):
    context={"status":"failed"}
    ids = request.POST.getlist('id[]')
    print ids
    for i in ids:
        roles = Role.objects.get(pk=i)
        roles.isApproved = "yes"
        roles.save()
    return JsonResponse(context,safe=False)

def viewCompany(request,value):
    context={"status":"failed"}
    print value
    company = Company.objects.get(id=value)
    print company
    company_json = company.as_json()
    print company_json
    return JsonResponse(company_json,safe=False)

def viewCompanyUser(request,value):
    context={"status":"failed"}
    print value
    company = Company.objects.get(id=value)
    print company
    company_json = company.as_jsonUser()
    print company_json
    return JsonResponse(company_json,safe=False)


def updateCompany(request,value):
    context={"status":"failed"}
    print value
    if Company.objects.get(id = value):
        print "update"
        results = Company.objects.get(id=value)
        form = CompanyForm(request.POST or None, request.FILES or None,instance=results)
        if form.is_valid():
            print "valid"
            form.save()
        print form
    else:
        print "new"
    return JsonResponse(context,safe=False)

def deleteCompany(request,value):
    context={"status":"failed"}
    print value
    Company.delete(Company.objects.get(id=value))
    print value
    return JsonResponse(context,safe=False)

def filterUser(request):
    context = {"status": "failed"}
    depts = str(request.GET.get('depts')).split(",")

    listOfUser = Role.objects.filter(isApproved="no", isDetailsProvided="yes", type="user")
    results = [ob.as_getEmail() for ob in listOfUser]

    resultSet = UserDetails.objects.filter(dept__in = depts,user__in = results).order_by('dept')
    results = [ob.as_filteredUser() for ob in resultSet]
    print results
    return JsonResponse(results, safe=False)

def filterAdmin(request):
    context = {"status": "failed"}
    depts = str(request.GET.get('depts')).split(",")


    listOfUser = Role.objects.filter(isApproved="no", isDetailsProvided="yes", type="admin")
    results = [ob.as_getEmail() for ob in listOfUser]

    resultSet = AdminDetails.objects.filter(dept__in = depts,user__in = results).order_by('dept')
    print resultSet
    results = [ob.as_filteredAdmin() for ob in resultSet]
    print results
    return JsonResponse(results, safe=False)


