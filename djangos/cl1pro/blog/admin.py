# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import blog,comment
# Register your models here.
admin.site.register(blog)
admin.site.register(comment)
