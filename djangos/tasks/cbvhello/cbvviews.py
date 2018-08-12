# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from cbvhello.models import school
# Create your views here.

class cbv1fun(View):
    def get(self,request):
        return HttpResponse("Hello world")

class cbv2fun(TemplateView):
    template_name ='cbvhello/cbvhelloworld.html'

    def get_context_data(self,**kwargs):
        context=super(cbv2fun,self).get_context_data(**kwargs)
        context['m1']='xyz'
        return context

class cbvlistclass(ListView):
    model = school
    template_name='cbvhello/cbvlist.html'

class cbvdetailclass(DetailView):
    context_object_name = 'school_details'
    model=school
    template_name='cbvhello/cbvdetail.html'

class cbvcreateclass(CreateView):
    model=school
    fields=('scname','principal','address')

class cbvupdateclass(UpdateView):
    model=school
    fields=('scname','principal')

class cbvdeleteclass(DeleteView):
    model=school
    success_url="/sclist"
