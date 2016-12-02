#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import os.path

for path in [ '/one/two/three','/1/2/3/Jollen', '/','.', '' ]:
    print '%15s : %s' %(path, os.path.basename(path))

