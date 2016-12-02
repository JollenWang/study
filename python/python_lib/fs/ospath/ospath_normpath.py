#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import os.path

list = ['one/two//three',
        '1/./2./3',
        '1/./2/./3',
        'one/../alt/two/three'
       ]
for path in list:
    print '%20s : %s' %(path, os.path.normpath(path))

