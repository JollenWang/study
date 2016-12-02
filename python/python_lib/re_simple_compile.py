#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import re

regexes = [ re.compile(p)
            for p in ['this', 'that' ]
            ]
text = 'Does this text match the pattern?'
print 'Text: %r\n' %text
print 'Text2: %s\n' %text

for regex in regexes:
    print 'seeking "%s"-->' %regex.pattern,
    if regex.search(text):
        print 'match!'
    else:
        print 'not match!'

