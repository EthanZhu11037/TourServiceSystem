# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-08 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_auto_20180708_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_num', models.CharField(max_length=5)),
                ('route_num', models.CharField(max_length=5)),
                ('stand_type', models.CharField(max_length=2)),
                ('stand_num', models.CharField(max_length=5)),
                ('sequence', models.IntegerField()),
                ('price', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ViewAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewspot_num', models.CharField(max_length=5)),
                ('time', models.DateTimeField()),
                ('people', models.IntegerField()),
            ],
        ),
    ]
