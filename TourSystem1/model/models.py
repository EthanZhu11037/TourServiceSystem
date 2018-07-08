# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tourist(models.Model):
    user_name = models.CharField(max_length=20)
    real_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    user_type = models.CharField(max_length=2, default='1')

class Company(models.Model):
    user_name = models.CharField(max_length=20)
    company_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    user_type = models.CharField(max_length=2, default='2')

class Administrator(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_type = models.CharField(max_length=2, default='3')

class ViewSpot(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    introduction = models.CharField(max_length=300, default='')
    time = models.CharField(max_length=100)
    price = models.IntegerField()

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

'''
'''