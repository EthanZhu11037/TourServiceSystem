# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-09 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_route_viewappointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='sequence',
        ),
        migrations.AlterField(
            model_name='route',
            name='stand_type',
            field=models.CharField(max_length=5),
        ),
    ]
