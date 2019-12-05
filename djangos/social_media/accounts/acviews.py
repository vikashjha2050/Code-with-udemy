# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from accounts import forms
from django.views.generic import CreateView, TemplateView


# Create your views here.
class signup(CreateView):
    form_class = forms.UserCreateForm
    success_url = '/login'
    template_name = "accounts/signup.html"

class thanks(TemplateView):
    template_name="accounts/thanks.html"
