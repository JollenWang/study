#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import collections

c = collections.Counter('abcdefgabc')
print "orignal c:", c

for letter in "abcdefgh":
    print '%s : %d' %(letter, c[letter])

