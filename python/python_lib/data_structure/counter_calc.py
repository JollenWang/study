#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import collections

c1 = collections.Counter(['a','b','c','a','b','b'])
c2 = collections.Counter('alphabet')

print 'C1', c1
print 'C2', c2

print '\nadd'
print c1 + c2

print '\nsub'
print c1 - c2

print '\ninsertion'
print c1 & c2

print '\nunion'
print c1 | c2




