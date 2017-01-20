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
	url(r'^new_topic/$', views.new_topic, name = 'new_topic'),
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name = 'new_entry'),
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name = 'edit_entry'),
]

