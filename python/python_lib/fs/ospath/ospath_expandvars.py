#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import os

os.environ['MYVAR'] = 'Jollen_Wang'
print os.path.expandvars('/path/to/$MYVAR')

