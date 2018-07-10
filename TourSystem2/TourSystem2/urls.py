"""TourSystem2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from model import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^home$',views.home),
    url(r'^regist$',views.regist),
    url(r'^regist/result$',views.regist_result),
    url(r'^login$',views.login),
    url(r'^login/result$', views.login_result),
    url(r'^logout$', views.logout),
    url(r'^addview$', views.addview),
    url(r'^addview/result$', views.addview_result),
    url(r'^view$', views.view),
    url(r'^view/search$', views.search_view),
    url(r'^view/detail/(?P<id>\d+)$',views.view_detail, name='viewspot_detail'),
    url(r'^view/edit/(?P<id>\d+)$',views.edit_view, name='edit_view'),
    url(r'^view/edit/result$',views.edit_view_result),
    url(r'^view/delete/(?P<id>\d+)$',views.delete_view, name='delete_view'),
    url(r'^route$', views.route),
    url(r'^addroute$', views.addroute),
    url(r'^addroute/result$', views.addroute_result),
]