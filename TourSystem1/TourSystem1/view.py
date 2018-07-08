# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from model.models import *

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def regist(request):
    return render(request, 'regist.html')

def regist_choose(request):
    user_type = request.POST['user_type']
    if user_type == 'tourist':
        return render(request, 'regist_tourist.html')
    elif user_type == 'company':
        return render(request, 'regist_company.html')
    elif user_type == 'administrator':
        return render(request, 'regist_administrator.html')
    else:
        return HttpResponse("<p>用户类型错误</p>")

def add_viewspot(request):
    return render(request, 'add_viewspot.html')