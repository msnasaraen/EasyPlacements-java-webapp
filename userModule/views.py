# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from samba.dcerpc.smb_acl import user

from .forms import UserForm,RoleForm,AdminForm
from django.http import HttpResponseRedirect
from .models import Role,AdminDetails
from django.shortcuts import redirect
# Create your views here.

def loginPage(request):
    return render(request,'userModule/login.html')

def provideDetailsUser(request):
    return render(request,'userModule/provideDetailsUser.html')

def provideDetailsAdmin(request):
    return render(request,'userModule/provideDetailsAdmin.html')

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
        else:
            form = AdminForm(request.POST,instance=results)
            if form.is_valid():
                form.save()
    else:
        form = AdminForm(data = request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.user = request.user
            admin.save()
    return JsonResponse(context)

def addUserDetails(request):
    context = {"status":"failed"}
    return context

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
                context = {
                    "status": "success",
                    "Details" : results[0],
                }

            else:
                context = {
                    "status": "failure",
                }
    return JsonResponse(context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def getDetails(request):

    if not request.user.is_authenticated():
        return render(request, 'userModule/login.html')
    else:
        data = {"status":"success","username":str(request.user)}
        return JsonResponse(data)





