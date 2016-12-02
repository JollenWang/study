#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import string

leet = string.maketrans('abcdefgh', '01234567')
s = 'The quick brown fox jumps over the lazy dog.'

print s
print s.translate(leet)



