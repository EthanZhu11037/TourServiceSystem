# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-10 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_viewspot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewspot',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]
