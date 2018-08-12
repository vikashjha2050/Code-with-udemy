# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from form1 import userform
# Create your views here.

def form_view_fun(request):
    formdata1=userform()
    if request.method=="POST":
        formdata=userform(request.POST)
        formdata.save(commit=True)
        return render(request,'form1.html',{'formmessage':formdata1})
    return render(request,'form1.html',{'formmessage':formdata1})
