#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import collections

c = collections.Counter()
print "initial", c

c.update("abcdefg")
print "Secquence", c

c.update({'a':1, 'd':5})
print "Dict", c

c.update(a=10,b=3)
print "Specfic", c
