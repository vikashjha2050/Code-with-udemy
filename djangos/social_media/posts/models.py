# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Post(models.Model):
    postcontent=models.CharField(max_length=1000)
    groupname=models.ForeignKey(Group, related_name='posts', on_delete=models.PROTECT)
    user=models.ForeignKey(User,related_name='posts', on_delete=models.PROTECT)

    def __str__(self):
        return self.postcontent
