# -*- coding: utf-8 -*-
from django.http import HttpResponse,Http404
from django.shortcuts import render,render_to_response
from model.models import *

def regist_tourist(request):
    request.encoding = 'utf-8'
    user_name = request.POST['user_name']
    real_name = request.POST['real_name']
    password = request.POST['password']
    phone = request.POST['phone']

    try:
        Tourist.objects.get(user_name=user_name)
    except Tourist.DoesNotExist:
        tourist = Tourist(user_name=user_name, real_name=real_name, password=password, phone=phone)
        tourist.save()
        return HttpResponse("<p>注册成功</p>")
    else:
        return HttpResponse("<p>该用户名已注册</p>")

def regist_company(request):
    request.encoding = 'utf-8'
    user_name = request.POST['user_name']
    company_name = request.POST['company_name']
    password = request.POST['password']
    phone = request.POST['phone']

    try:
        Company.objects.get(user_name=user_name)
    except Company.DoesNotExist:
        company = Company(user_name=user_name, company_name=company_name, password=password, phone=phone)
        company.save()
        return HttpResponse("<p>注册成功</p>")
    else:
        return HttpResponse("<p>该用户名已注册</p>")

def regist_administrator(request):
    request.encoding = 'utf-8'
    user_name = request.POST['user_name']
    password = request.POST['password']

    try:
        Administrator.objects.get(user_name=user_name)
    except Administrator.DoesNotExist:
        administrator = Administrator(user_name=user_name, password=password)
        administrator.save()
        return HttpResponse("<p>注册成功</p>")
    else:
        return HttpResponse("<p>该用户名已注册</p>")

def login_result(request):
    request.encoding = 'utf-8'
    user_name = request.POST['user_name']
    password = request.POST['password']
    user_type = request.POST['user_type']

    if user_type == 'tourist':
        user = Tourist.objects.filter(user_name__exact=user_name, password__exact=password)
    elif user_type == 'company':
        user = Company.objects.filter(user_name__exact=user_name, password__exact=password)
    elif user_type == 'administrator':
        user = Administrator.objects.filter(user_name__exact=user_name, password__exact=password)

    if user:
        return HttpResponse("<p>登录成功</p>")
    else:
        return HttpResponse("<p>用户名或密码有误</p>")

def add_viewspot_result(request):
    request.encoding = 'utf-8'
    name = request.POST['name']
    address = request.POST['address']
    introduction = request.POST['introduction']
    time = request.POST['time']
    price = request.POST['price']

    try:
        ViewSpot.objects.get(name=name)
    except ViewSpot.DoesNotExist:
        viewspot = ViewSpot(name=name, address=address, introduction=introduction, time=time, price=price)
        viewspot.save()
        return HttpResponse("<p>添加景点成功</p>")
    else:
        return HttpResponse("<p>该景点已存在</p>")

def viewspot(request):
    viewspot_list = ViewSpot.objects.all()
    return render(request, 'viewspot.html', {'viewspot_list': viewspot_list})

def viewspot_edit1(request):
    viewspot_list = ViewSpot.objects.all()
    return render(request, 'viewspot_edit1.html', {'viewspot_list': viewspot_list})

def viewspot_edit2(request, id):
    viewspot = ViewSpot.objects.get(id=id)
    return render(request, 'viewspot_edit2.html', {'viewspot': viewspot})

def viewspot_edit3(request):
    request.encoding = 'utf-8'
    name = request.POST['name']
    address = request.POST['address']
    introduction = request.POST['introduction']
    time = request.POST['time']
    price = request.POST['price']

    ViewSpot.objects.get(name=name)
    ViewSpot.objects.filter(name=name).update(name=name, address=address, introduction=introduction, time=time, price=price)
    return HttpResponse("<p>修改景点成功</p>")

def viewspot_delete(request):
    viewspot_list = ViewSpot.objects.all()
    return render(request, 'viewspot_delete.html', {'viewspot_list': viewspot_list})

def viewspot_delete_result(request,id):
    request.encoding = 'utf-8'
    ViewSpot.objects.filter(id=id).delete()
    return HttpResponse("<p>删除景点成功</p>")

def detail(request,id):
    try:
        viewspot = ViewSpot.objects.get(id=id)
    except viewspot.DoesNotExist:
        raise Http404
    return render(request, 'viewspot_detail.html', locals())

def viewspot_search(request):
    request.encoding = 'utf-8'
    keyword = request.POST['keyword']

    try:
        viewspot_result = ViewSpot.objects.filter(name__contains=keyword)
    except viewspot.DoesNotExist:
        return HttpResponse("<p>无搜索结果</p>")
    else:
        return render(request, 'viewspot_search.html', {'viewspot_result': viewspot_result})

def add_route2(request):
    request.encoding = 'utf-8'
    company_num = request.POST['company_num']
    route_num = request.POST['route_num']
    stand_type = request.POST['stand_type']

    if stand_type == '1':
        stand_list = ViewSpot.objects.all()
    elif stand_type == '2':
        stand_list = Restaurant.objects.all()
    elif stand_type == '3':
        stand_list = Hotel.objects.all()
    else:
        return HttpResponse("<p>站点类型有误</p>")

    return render(request, 'add_route2.html', {'company_num': company_num, 'route_num': route_num, 'stand_type': stand_type, 'stand_list': stand_list})

def add_route3(request):
    request.encoding = 'utf-8'
    company_num = request.POST['company_num']
    route_num = request.POST['route_num']
    stand_type = request.POST['stand_type']
    stand_num = request.POST['stand_num']
    price = request.POST['price']
    time = request.POST['time']

    # try:
    #     Route.objects.get(company_num=company_num, route_num=route_num)
    # except Route.DoesNotExist:
    route = Route(company_num=company_num, route_num=route_num, stand_type=stand_type, stand_num=stand_num,
                        price=price, time=time)
    route.save()
    return HttpResponse("<p>添加路线节点成功</p>")
