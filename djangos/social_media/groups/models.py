# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()

# Create your models here.
class group(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True)
    members=models.ManyToManyField(user)

    def __str__(self):
        return self.name

class group_members(models.Model):
    group1=models.ForeignKey(group, on_delete=models.PROTECT)
    member1=models.ForeignKey(user,related_name='group_member', on_delete=models.PROTECT)

    def __str__(self):
        return self.member1.username
