#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import re

text = 'aabbbbaabccdaabcdateg'
pattern = 'ab'

for match in re.findall(pattern, text):
    print 'found "%s"' %(match)

