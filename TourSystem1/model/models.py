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

class Route(models.Model):
    company_num = models.CharField(max_length=5)#公司编号
    route_num = models.CharField(max_length=5)#公司路线编号
    stand_type = models.CharField(max_length=5)#节点类型
    stand_num = models.CharField(max_length=5)#节点编号
    # sequence = models.IntegerField()#节点顺序
    price = models.IntegerField()#路线价格
    time = models.DateTimeField()#游览时间

class ViewAppointment(models.Model):
    viewspot_num = models.CharField(max_length=5)
    time = models.DateTimeField()
    people = models.IntegerField()

'''
'''