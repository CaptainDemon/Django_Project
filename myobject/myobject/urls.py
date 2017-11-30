from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [

    url(r'^myadmin/',include('myadmin.urls')),#网站后台路由
    url(r'^',include('myweb.urls')),#网站前台路由


]
