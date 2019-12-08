# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from groups import models
from django.views.generic import CreateView, ListView, DetailView, RedirectView
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

class create_group(CreateView):
    model=models.Group
    fields={'name','description'}
    success_url='/groups-list'

class groups_list(ListView):
    model=models.Group
    template_name='groups/group_list.html'

class group_detail(DetailView):
    context_object_name = 'group_details'
    model=models.Group
    template_name='groups/detailgroup.html'

def group_join(requests,pk):
    group2 = get_object_or_404(models.Group,pk=pk)
    print(requests.user)
    group2.members.add(requests.user)
    return redirect('group_detail', pk=pk)

def group_leave(requests,pk):
    group2 = get_object_or_404(models.Group,pk=pk)
    group2.members.remove(requests.user)
    print(requests.user, type(requests.user))
    return redirect('group_detail', pk=pk)
