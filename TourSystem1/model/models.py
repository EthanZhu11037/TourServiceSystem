# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tourist(models.Model):
    user_name = models.CharField(max_length=20)
    real_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)