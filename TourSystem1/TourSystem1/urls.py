"""TourSystem1 URL Configuration

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
from . import view,dbrequest

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home$', view.home),
    url(r'^login$', view.login),
    url(r'^regist_1$', view.regist),
    url(r'^regist_2$', view.regist_choose),
    url(r'^regist_tourist$', dbrequest.regist_tourist),
    url(r'^regist_company$', dbrequest.regist_company),
    url(r'^regist_administrator$', dbrequest.regist_administrator),
    url(r'^login_result$', dbrequest.login_result),
    url(r'^add_viewspot$', view.add_viewspot),
    url(r'^add_viewspot_result$', dbrequest.add_viewspot_result),
    url(r'^viewspot_edit2/viewspot_edit3$', dbrequest.viewspot_edit3, name='viewspot_edit3'),
    url(r'^viewspot$', dbrequest.viewspot),
    url(r'^viewspot_edit1$', dbrequest.viewspot_edit1),
    url(r'^viewspot_edit2/(?P<id>\d+)$', dbrequest.viewspot_edit2, name='viewspot_edit2'),
    url(r'^viewspot_delete$', dbrequest.viewspot_delete),
    url(r'^viewspot_delete_result/(?P<id>\d+)$', dbrequest.viewspot_delete_result, name='viewspot_delete_result'),
    url(r'^(?P<id>\d+)/$',dbrequest.detail,name='viewspot_detail'),
    url(r'^viewspot_search$', dbrequest.viewspot_search),
]
