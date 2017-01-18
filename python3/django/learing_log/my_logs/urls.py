#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

from django.conf.urls import url
from . import views

#define my_logs's URL mode

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^topics/$', views.topics, name = 'topics'),
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
]

