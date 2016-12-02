#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)
start = match.start()
end = match.end()

print 'Found "%s"\r\nin "%s"\r\nform %d to %d.' %(match.re.pattern, match.string, start, end)

