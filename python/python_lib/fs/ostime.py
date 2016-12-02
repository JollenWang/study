#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import os.path
import time

print 'File          :', __file__
print 'Access Time   :', time.ctime(os.path.getatime(__file__))
print 'Modified Tine :', time.ctime(os.path.getmtime(__file__))
print 'Change Tine   :', time.ctime(os.path.getctime(__file__))
print 'Size          :', os.path.getsize(__file__)

