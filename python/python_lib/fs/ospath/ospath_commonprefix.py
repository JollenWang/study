#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import os.path

paths = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/three/',
        ]
for path in paths:
    print 'PATH:', path
print

print 'COMMON_PREFIX:', os.path.commonprefix(paths)
