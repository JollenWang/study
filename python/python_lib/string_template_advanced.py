#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import string

template_text = '''
    Item_a : %abc_def
    Item_b : %%
    Item_c : %with_underscore
    Item_d : %notunderscored
'''

d = {
    'abc_def'         : 'A',
    'with_underscore' : 'Jollen',
    'notunderscored'  : 'June',
}

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

t = MyTemplate(template_text)
print "Modified ID pattern:"
print t.safe_substitute(d)
print MyTemplate(template_text).safe_substitute(d)

