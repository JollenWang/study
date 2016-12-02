#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import textwrap
from sample_text import stext

print 'No dedent:\n'
print textwrap.fill(stext, width=50)
print 'dedent:\n'
print textwrap.dedent(stext)

dedented_text = textwrap.dedent(stext).strip()
for width in [ 45, 70 ]:
    print '%d columns:\n' %width
    print textwrap.fill(dedented_text, width = width)
    print

print 'Text with prefix:'
print textwrap.fill(dedented_text,
                    initial_indent = ' ',
                    subsequent_indent = '$> ',
                    width = 50)

