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
        return render(request, 'register.html', ctx)

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
            return render(request, 'register.html', ctx)
        ctx['rlt'] = "注册成功"
        return render(request, 'register.html', ctx)
    else:
        ctx['rlt'] = "该用户名已注册"
        return render(request, 'register.html', ctx)

def login_result(request):
    ctx = {}
    request.encoding = 'utf-8'
    username = request.POST['username']
    password = request.POST['password']
    # print username, password
    re = auth.authenticate(username=username, password=password)
    if re is not None:
        auth.login(request, re)
        if re.is_tourist == True:
            return redirect('/tourist', {'user': re})
        elif re.is_company == True:
            return redirect('/route', {'user': re})
        elif  re.is_adminis == True:
            return redirect('/view', {'user': re})
        else:
            return render(request, 'login.html')
    else:
        ctx['rlt'] = "用户名或密码错误"
        return render(request, 'login.html', ctx)

def logout(request):
    auth.logout(request)
    return render(request,'home.html')

def view(request):
    viewspot_list = ViewSpot.objects.all()
    return render(request, 'view.html', {'viewspot_list': viewspot_list})

def addview(request):
    return render(request, 'addviewinfo.html')

def addview_result(request):
    ctx = {}
    request.encoding = 'utf-8'
    name = request.POST['name']
    address = request.POST['address']
    intro = request.POST['intro']
    time = request.POST['time']
    price = request.POST['price']

    try:
        ViewSpot.objects.get(name=name)
    except ViewSpot.DoesNotExist:
        viewspot = ViewSpot(name=name, address=address, intro=intro, time=time, price=price)
        viewspot.save()
        # !!!!!!少提示!!!!!!
        viewspot_list = ViewSpot.objects.all()
        return render(request, 'view.html', {'viewspot_list': viewspot_list})
    else:
        ctx['rlt'] = "该景点已存在"
        return render(request, 'addviewinfo.html', ctx)

def search_view(request):
    ctx = {}
    request.encoding = 'utf-8'
    keyword = request.POST['keyword']

    if keyword == '':
        viewspot_list = ViewSpot.objects.all()
        return render(request, 'view.html', {'viewspot_list': viewspot_list})
        # ctx['rlt'] = "无搜索结果"
        # return render(request, 'view.html', ctx)
    viewspot_list = ViewSpot.objects.filter(name__contains=keyword)
    return render(request, 'view.html', {'viewspot_list': viewspot_list})

def view_detail(request, id):
    view = ViewSpot.objects.get(id=id)
    va_list = ViewAppointment.objects.filter(view_name=view.name)
    return render(request, 'viewdetail.html', {'view': view, 'va_list':va_list})

def edit_view(request, id):
    view = ViewSpot.objects.get(id=id)
    return render(request, 'editview.html', {'view': view})

def edit_view_result(request):
    request.encoding = 'utf-8'
    id = request.POST['id']
    name = request.POST['name']
    address = request.POST['address']
    intro = request.POST['intro']
    time = request.POST['time']
    price = request.POST['price']

    ViewSpot.objects.filter(id=id).update(name=name, address=address, intro=intro, time=time, price=price)

    viewspot_list = ViewSpot.objects.all()
    return render(request, 'view.html', {'viewspot_list': viewspot_list})

def delete_view(request, id):
    ViewSpot.objects.filter(id=id).delete()
    viewspot_list = ViewSpot.objects.all()
    # !!!!!!少提示!!!!!!
    return render(request, 'view.html', {'viewspot_list': viewspot_list})

def route(request):
    company_name = request.user.username
    # print  company_name
    route_list = Route.objects.filter(company_name=company_name).order_by('route_num')
    return render(request, 'route.html',{'route_list': route_list})

def addroute(request):
    viewspot_list = ViewSpot.objects.all()
    return render(request, 'addroute.html', {'viewspot_list': viewspot_list})

def addroute_result(request):
    ctx = {}
    request.encoding = 'utf-8'
    company_name = request.POST['company_name']
    route_num = request.POST['route_num']
    stand_num = request.POST['stand_num']
    stand_1_name = request.POST['stand_1_name']
    date_1 = request.POST['date_1']
    stand_2_name = request.POST['stand_2_name']
    date_2 = request.POST['date_2']
    stand_3_name = request.POST['stand_3_name']
    date_3 = request.POST['date_3']
    stand_4_name = request.POST['stand_4_name']
    date_4 = request.POST['date_4']
    price = request.POST['price']
    end = request.POST['end']

    try:
        Route.objects.get(company_name=company_name, route_num=route_num)
    except Route.DoesNotExist:
        route = Route(company_name=company_name, route_num=route_num, stand_num=stand_num, stand_1_name=stand_1_name,
                      date_1=date_1, stand_2_name=stand_2_name, date_2=date_2, stand_3_name=stand_3_name,
                      date_3=date_3, stand_4_name=stand_4_name, date_4=date_4, price=price, end=end)
        route.save()
        # !!!!!!少提示!!!!!!
        company_name = request.user.username
        route_list = Route.objects.filter(company_name=company_name)
        return render(request, 'route.html', {'route_list': route_list})
    else:
        ctx['rlt'] = "该路线已存在"
        return render(request, 'addroute.html', ctx)

def tourist(request):
    return render(request, 'tourist.html')

def route2(request):
    route_list = Route.objects.all()
    tourist_name = request.user.username
    ra_list = RouteAppointment.objects.filter(tourist_name=tourist_name)
    return render(request, 'route_tourist.html',{'route_list': route_list, 'ra_list': ra_list})

def route_detail(request, id):
    route = Route.objects.get(id=id)
    ra_list = RouteAppointment.objects.filter(company_name=request.user.username, route_num=route.route_num)
    return render(request, 'routedetail.html', {'route': route, 'ra_list':ra_list})

def route_detail_tourist(request, id):
    route = Route.objects.get(id=id)
    return render(request, 'routedetail_tourist.html', {'route': route})

def make_appointment(request, id):
    r = Route.objects.get(id=id)
    company_name = r.company_name
    route_num = r.route_num
    tourist_name = request.user.username
    # print company_name,route_num,tourist_name
    try:
        RouteAppointment.objects.get(company_name=company_name, route_num=route_num, tourist_name=tourist_name)
    except RouteAppointment.DoesNotExist:
        ra = RouteAppointment(company_name=company_name, route_num=route_num, tourist_name=tourist_name)
        ra.save()
        item = Route.objects.get(company_name=company_name, route_num=route_num)
        new_num = item.person_num
        new_num = new_num + 1
        item.person_num = new_num
        item.save()

        if item.stand_1_name != '':
            try:
                raw = ViewAppointment.objects.get(view_name=item.stand_1_name, date=item.date_1)
            except ViewAppointment.DoesNotExist:
                va = ViewAppointment(view_name=item.stand_1_name, date=item.date_1, person_num=1)
                va.save()
            else:
                num = raw.person_num
                num = num + 1
                raw.person_num = num
                raw.save()

    route_list = Route.objects.all()
    tourist_name = request.user.username
    ra_list = RouteAppointment.objects.filter(tourist_name=tourist_name)
    return render(request, 'route_tourist.html', {'route_list': route_list, 'ra_list': ra_list})

def edit_route(request, id):
    route = Route.objects.get(id=id)
    return render(request, 'editroute.html', {'route': route})

def edit_route_result(request):
    request.encoding = 'utf-8'
    id = request.POST['id']
    company_name = request.POST['company_name']
    route_num = request.POST['route_num']
    stand_num = request.POST['stand_num']
    stand_1_name = request.POST['stand_1_name']
    date_1 = request.POST['date_1']
    stand_2_name = request.POST['stand_2_name']
    date_2 = request.POST['date_2']
    stand_3_name = request.POST['stand_3_name']
    date_3 = request.POST['date_3']
    stand_4_name = request.POST['stand_4_name']
    date_4 = request.POST['date_4']
    price = request.POST['price']
    end = request.POST['end']

    Route.objects.filter(id=id).update(route_num=route_num, stand_num=stand_num, stand_1_name=stand_1_name,
                                       date_1=date_1, stand_2_name=stand_2_name, date_2=date_2, stand_3_name=stand_3_name,
                                       date_3=date_3, stand_4_name=stand_4_name, date_4=date_4, price=price, end=end)

    company_name = request.user.username
    route_list = Route.objects.filter(company_name=company_name).order_by('route_num')
    return render(request, 'route.html',{'route_list': route_list})

def delete_route(request, id):
    Route.objects.filter(id=id).delete()
    company_name = request.user.username
    route_list = Route.objects.filter(company_name=company_name).order_by('route_num')
    # !!!!!!少提示!!!!!!
    return render(request, 'route.html', {'route_list': route_list})