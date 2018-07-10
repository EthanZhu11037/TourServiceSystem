# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-10 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_viewspot_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('route_num', models.CharField(max_length=20)),
                ('stand_num', models.IntegerField(default=1)),
                ('stand_1_name', models.CharField(max_length=100)),
                ('date_1', models.DateField()),
                ('stand_2_name', models.CharField(max_length=100, null=True)),
                ('date_2', models.DateField(null=True)),
                ('stand_3_name', models.CharField(max_length=100, null=True)),
                ('date_3', models.DateField(null=True)),
                ('stand_4_name', models.CharField(max_length=100, null=True)),
                ('date_4', models.DateField(null=True)),
                ('person_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RouteAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('route_num', models.CharField(max_length=20)),
                ('tourist_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ViewAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('person_num', models.IntegerField(default=0)),
            ],
        ),
    ]
