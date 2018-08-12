# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def inheri_fun(request):
    return render(request,'templateinheri/inheri1.html')
