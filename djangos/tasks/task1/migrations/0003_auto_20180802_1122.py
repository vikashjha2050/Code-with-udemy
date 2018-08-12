# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-02 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_auto_20180802_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='udb',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]