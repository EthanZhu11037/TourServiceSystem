# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,Http404
from .models import *
from django.contrib import auth
from django import forms
from django.contrib.auth.models import AbstractUser,User

# Create your views here.

def home(request):
    return render(request,'home.html')

def regist(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def regist_result(request):
    ctx = {}
    request.encoding = 'utf-8'
    usertype = request.POST['usertype']
    username = request.POST['username']
    password = request.POST['password']

    if username == "" or password == "":
        ctx['rlt'] = "用户名或密码为空"
        return render(request, "register.html", ctx)

    try:
        UserInfo.objects.get(username=username)
    except UserInfo.DoesNotExist:
        if usertype == 'tourist':
            user = UserInfo.objects.create_user(username=username, password=password, is_tourist=True)
        elif usertype == 'company':
            user = UserInfo.objects.create_user(username=username, password=password, is_company=True)
        elif usertype == 'adminis':
            user = UserInfo.objects.create_user(username=username, password=password, is_adminis=True)
        else:
            ctx['rlt'] = "用户类型有误"
            return render(request, "register.html", ctx)
        ctx['rlt'] = "注册成功"
        return render(request, "register.html", ctx)
    else:
        ctx['rlt'] = "该用户名已注册"
        return render(request, "register.html", ctx)

def login_result(request):
    ctx = {}
    request.encoding = 'utf-8'
    username = request.POST['username']
    password = request.POST['password']
    print username, password
    re = auth.authenticate(username=username, password=password)
    if re is not None:
        auth.login(request, re)
        return redirect('/', {'user': re})
        # return render(request, "home.html")
    else:
        ctx['rlt'] = "用户名或密码错误"
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return render(request,'home.html')