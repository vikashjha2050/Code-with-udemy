# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class school(models.Model):
    scname=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.scname

    def get_absolute_url(self):
        return reverse("detail",kwargs={'pk':self.pk})


class student(models.Model):
    name=models.CharField(max_length=100)
    schoolname=models.ForeignKey(school,related_name='students')

    def __str__(self):
        return self.name
