# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def filter_fun(request):
    dict1={'key1':'hello value1','key2':100}
    return render(request,'filterapp/filter1.html',dict1)
