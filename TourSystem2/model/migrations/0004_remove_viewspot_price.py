# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-10 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_auto_20180710_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewspot',
            name='price',
        ),
    ]
