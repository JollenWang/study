#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import string

s0 = string.Template('The $a and $b')
print s0.substitute(a = 'apple', b = 'pear')

d = {'a' : 'Jollen', 'b' : 'June'}
print s0.substitute(d)

