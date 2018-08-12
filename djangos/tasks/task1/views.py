# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from task1.models import udb,userdb
# Create your views here.

def index(request):
    username1=udb.objects.all()
    userdict={'usermessage':username1}
    return render(request,'index.html',context=userdict)

def userfun(request):
    users=userdb.objects.all()
    userdict={'usersm':users}
    return render(request,'user.html',context=userdict)
