from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from model.models import Tourist

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def regist(request):
    return render(request, 'regist.html')

def regist_result(request):
    request.encoding = 'utf-8'
    tourist = Tourist(user_name=request.POST['user_name'], real_name=request.POST['real_name'],
                          password=request.POST['password'], phone=request.POST['phone'])
    tourist.save()
    return HttpResponse("<p>Regist Succeed!</p>")

def login_result(request):
    request.encoding = 'utf-8'
    user_name = request.POST['user_name']
    password = request.POST['password']
    user = Tourist.objects.filter(user_name__exact=user_name, password__exact=password)
    if user:
        return HttpResponse("<p>Login Succeed!</p>")
    else:
        return HttpResponse("<p>Username or Password ERROR!</p>")