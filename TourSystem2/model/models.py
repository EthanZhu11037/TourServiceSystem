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