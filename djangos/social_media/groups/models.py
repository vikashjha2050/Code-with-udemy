# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()

# Create your models here.
class Group(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True)
    members=models.ManyToManyField(user, related_name='allgroups')

    def __str__(self):
        return self.name
