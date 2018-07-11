# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserInfo(AbstractUser):
    is_tourist = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_adminis = models.BooleanField(default=False)
    realname = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=11, null=True)

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.username

class ViewSpot(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    intro = models.CharField(max_length=500)
    time = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)

class Route(models.Model):
    company_name = models.CharField(max_length=150)
    route_num = models.CharField(max_length=20)
    stand_num = models.IntegerField(default=0)
    stand_1_name = models.CharField(max_length=100, null=True)
    date_1 = models.DateField(null=True)
    stand_2_name = models.CharField(max_length=100, null=True)
    date_2 = models.DateField(null=True)
    stand_3_name = models.CharField(max_length=100, null=True)
    date_3 = models.DateField(null=True)
    stand_4_name = models.CharField(max_length=100, null=True)
    date_4 = models.DateField(null=True)
    person_num = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    end = models.DateField(null=True)

class RouteAppointment(models.Model):
    company_name = models.CharField(max_length=150)
    route_num = models.CharField(max_length=20)
    tourist_name = models.CharField(max_length=150)

class ViewAppointment(models.Model):
    view_name = models.CharField(max_length=100)
    date = models.DateField()
    person_num = models.IntegerField(default=0)
