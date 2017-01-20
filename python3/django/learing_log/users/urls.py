#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
	url(r'^login/$', login, {'template_name' : 'users/login.html'}, name = 'login'),
]

