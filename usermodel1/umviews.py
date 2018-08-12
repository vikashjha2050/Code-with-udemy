# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from usermodel1.umforms import userform,userinfo1
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def um_register(request):
    registered = False
    if request.method=='POST':
        um1=userform(request.POST)
        um2=userinfo1(request.POST)
        if um1.is_valid() and um2.is_valid():

            umm1=um1.save()
            umm1.set_password(umm1.password)
            umm1.save()

            umm2=um2.save(commit=False)
            umm2.user=umm1
            if 'profile_pic' in request.FILES:
                umm2.profile_pic=request.FILES['profile_pic']
            umm2.save()
            print(umm2)
            registered = True
        else:
            print(um1.errors,um2.errors)
    else:
        um1=userform()
        um2=userinfo1()
    return render(request,'usermodel1/register1.html',{'um1':um1,'um2':um2,'registered':registered})

def user_login(request):
    if request.method=='POST':
        u1=request.POST.get('u1')
        p1=request.POST.get('p1')
        print request.POST
        user=authenticate(username=u1,password=p1)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid data")

    else:
        return render(request, 'usermodel1/login1.html', {})
