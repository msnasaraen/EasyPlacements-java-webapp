# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from samba.dcerpc.smb_acl import user

from .forms import UserForm,RoleForm,AdminForm,UserDetailsForm
from django.http import HttpResponseRedirect
from .models import Role,AdminDetails,UserDetails
from django.shortcuts import redirect
# Create your views here.

def loginPage(request):
    return render(request,'userModule/login.html')

def provideDetailsUser(request):
    return render(request,'userModule/provideDetailsUser.html')

def provideDetailsAdmin(request):
    return render(request,'userModule/provideDetailsAdmin.html')

def notApprovedAdmin(request):
    return render(request,'userModule/notApprovedAd.html')

def notApprovedUser(request):
    return render(request,'userModule/notApprovedUser.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")


def getAdminDetails(request):
    context = {"status":"failed"}
    if AdminDetails.objects.filter(user=request.user):
        adminDetails = AdminDetails.objects.filter(user=request.user)
        #print adminDetails.profilepicture.url
        results = [ro.as_jsonValue() for ro in adminDetails]
        print results[0]
        context = results[0]
    return JsonResponse(context)

def getUserDetails(request):
    context = {"status":"failed"}
    if UserDetails.objects.filter(user=request.user):
        userresult = UserDetails.objects.filter(user=request.user)

        results = [ro.as_jsonUser() for ro in userresult]
        print results[0]
        context = results[0]
    return JsonResponse(context)


def addAdminDetails(request):
    context = {"status":"failed"}
    print request.POST
    print request.FILES
    if AdminDetails.objects.filter(user=request.user):
        results = AdminDetails.objects.get(user=request.user)
        if request.FILES:
            results.profilepicture = request.FILES['profilepicture']
            results.save()
            print "one hi"
            roles = Role.objects.get(user=request.user)
            roles.isDetailsProvided="yes"
            roles.save()
            if Role.objects.get(user=request.user).isApproved=="yes":
                return HttpResponseRedirect("http://127.0.0.1:8000/placements/companyDetail/")
            else:
                return HttpResponseRedirect("http://127.0.0.1:8000/user/notApprovedAdmin/")
        elif request.POST:
            form = AdminForm(request.POST,instance=results)
            if form.is_valid():
                form.save()
            if results.profilepicture:
                if Role.objects.get(user=request.user).isApproved == "yes":
                    return HttpResponseRedirect("http://127.0.0.1:8000/placements/companyDetail/")
                else:
                    return HttpResponseRedirect("http://127.0.0.1:8000/user/notApprovedAdmin/")
    else:
        form = AdminForm(data = request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.user = request.user
            admin.save()
    return JsonResponse(context)

def addUserDetails(request):
    context = {"status":"failed"}
    print request.POST
    print request.FILES
    print "level1"
    if UserDetails.objects.filter(user=request.user):
        results = UserDetails.objects.get(user=request.user)
        print "level2"
        if request.FILES:
            print "level3"
            results.profilepicture = request.FILES['profilepicture']
            results.resume = request.FILES['resume']
            results.save()
            roles = Role.objects.get(user=request.user)
            roles.isDetailsProvided = "yes"
            roles.save()
            if Role.objects.get(user=request.user).isApproved=="yes":
                return HttpResponseRedirect("http://127.0.0.1:8000/placements/usercompanyDetail/")
            else:
                return HttpResponseRedirect("http://127.0.0.1:8000/user/notApprovedUser/")
        else:
            print "level4"
            print request.POST
            form = UserDetailsForm(request.POST, instance=results)
            print form
            if form.is_valid():
                form.save()
            if results.profilepicture:
                if Role.objects.get(user=request.user).isApproved == "yes":
                    return HttpResponseRedirect("http://127.0.0.1:8000/placements/usercompanyDetail/")
                else:
                    return HttpResponseRedirect("http://127.0.0.1:8000/user/notApprovedUser/")

    else:
        form = UserDetailsForm(data=request.POST)
        if form.is_valid():
            print "three"
            admin = form.save(commit=False)
            admin.user = request.user
            admin.save()
        return JsonResponse(context)


def register(request):
    print request.POST
    form = UserForm(request.POST)
    context ={"status": "failed"}
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        if user is not None:
            roleform = RoleForm(request.POST)
            print roleform
            if roleform.is_valid():
                role = roleform.save(commit=False)
                role.user = user
                role.isApproved = "no"
                role.save()
                if user.is_active:
                    login(request, user)
                    details = {"role": request.POST.get('type'),
                               "username": username,
                               "approved": "no"}
                    context = {
                        "status": "success",
                        "Details" : details

                    }
                else:
                    context = {
                        "status": "failure",
                    }
    return JsonResponse(context)

def login_user(request):
    context ={"status": "failed"}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                role = Role.objects.filter(user=user)
                results = [ro.as_json() for ro in role]
                print results[0]
                if results[0].get('isDetailsProvided')=='yes':
                    context = {
                        "status": "success",
                        "Details": results[0],
                        "provides": "yes"
                    }
                else:
                    context = {
                        "status": "success",
                        "Details": results[0],
                        "provides": "no"
                    }

            else:
                context = {
                    "status": "failure",
                }
    return JsonResponse(context)

def getDetails(request):

    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        username = str(request.user)
        role = Role.objects.filter(user=request.user)
        results = [ro.as_json() for ro in role]
        profilepicture = "/imges/img.jpg"
        print results[0].get('type')
        type = str(results[0].get('type'))
        if(type=="admin") and AdminDetails.objects.filter(user=request.user):
            results = AdminDetails.objects.get(user=request.user)
            profilepicture = str(results.profilepicture.url)
        elif UserDetails.objects.filter(user=request.user):
            results = UserDetails.objects.get(user=request.user)
            profilepicture = str(results.profilepicture.url)
        data = {"status":"success","username":username,"type":type,"profilepicture":profilepicture}
        return JsonResponse(data)



