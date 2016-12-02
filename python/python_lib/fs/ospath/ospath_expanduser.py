#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import os.path

for user in ['', 'xkwang', 'workspace']:
    lookup = '~' + user
    print '%12s : %s' %(lookup, os.path.expanduser(lookup))

