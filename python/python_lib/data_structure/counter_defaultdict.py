#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import collections

def default_factory():
    return 'default value'

d = collections.defaultdict(default_factory, foo = 'A', bar = 'B')
print 'd:', d
print 'foo=>', d['foo']
print 'bar=>', d['bar']
print 'Jollen=>', d['A']
