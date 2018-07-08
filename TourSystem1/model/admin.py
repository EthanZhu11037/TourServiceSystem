# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from model.models import Tourist,Company,Administrator

# Register your models here.
admin.site.register(Tourist)
admin.site.register(Company)
admin.site.register(Administrator)