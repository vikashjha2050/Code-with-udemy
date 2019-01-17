# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-16 11:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180816_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='groupname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='groups.group'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postcontent',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
