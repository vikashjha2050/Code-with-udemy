# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def rel_view_fun(request):
    return render(request,'relative_url/relativetemplate.html')

def rel_base_fun(request):
    return render(request,'relative_url/base1.html')
