#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import collections

c = collections.Counter('extremely')
c['z'] = 0

print c
print list(c.elements())

