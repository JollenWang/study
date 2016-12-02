#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import os.path

parts = [('one','two','three'),
         ('/one','two','three'),
         ('/','1','2','3'),
         ('/1','/2','/3')
        ]

for path in parts:
    print '%20s : %s' %(path, os.path.join(*path))

