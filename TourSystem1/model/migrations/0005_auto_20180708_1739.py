# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-08 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0004_hotel_restaurant_viewspot'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewspot',
            name='introduction',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='viewspot',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
