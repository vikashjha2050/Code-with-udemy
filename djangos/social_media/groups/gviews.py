# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from groups import models
from django.views.generic import CreateView, ListView, DetailView, RedirectView
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

class create_group(CreateView):
    model=models.group
    fields={'name','description'}
    success_url='/'

class groups_list(ListView):
    model=models.group
    template_name='groups/group_list.html'

class group_detail(DetailView):
    context_object_name = 'group_details'
    model=models.group
    template_name='groups/detailgroup.html'

def group_join(requests,pk):
    group2 = get_object_or_404(models.group,pk=pk)
    models.group_members.objects.create(member1=requests.user,group1=group2)
    return redirect('group_detail', pk=pk)

def group_leave(requests,pk):
    group2 = get_object_or_404(models.group,pk=pk)
    gm1=models.group_members.objects.get(member1=requests.user,group1=group2)
    print(gm1)
    gm1.delete()
    return redirect('group_detail', pk=pk)
