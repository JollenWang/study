#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import string

values = {'var' : 'foo'}

t = string.Template("""
Variable    : $var
Escape      : $$
Variable in Text : ${var}iable
""")

print 'TEMPLATE:', t.substitute(values)
s = """
Varaible    : %(var)s
Escape      : %%
Variable in tex : %(var)siable
"""

print 'INTERPOLATION:', s % values



