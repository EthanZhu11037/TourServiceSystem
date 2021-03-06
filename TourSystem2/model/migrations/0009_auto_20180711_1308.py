# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-11 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0008_route_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='date_1',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='date_2',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='date_3',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='date_4',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='stand_1_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='stand_num',
            field=models.IntegerField(default=0),
        ),
    ]
