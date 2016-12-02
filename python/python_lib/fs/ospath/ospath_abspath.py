#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import os.path

list = ['.','..','./1/2/3','../1/2/3']
for path in list:
    print '%17s : %s' %(path, os.path.abspath(path))
