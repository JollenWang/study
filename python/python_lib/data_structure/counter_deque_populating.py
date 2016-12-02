#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import collections

#add to the right
d1 = collections.deque()

d1.extend('abcdefg')
print 'extend right:', d1
d1.append('h')
print 'append right:', d1

#add to the left
d2 = collections.deque()

d2.extendleft(xrange(6))
print 'extend left:', d2
d2.appendleft(6)
print 'append left:', d2





