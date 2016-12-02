#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import glob

for name in glob.glob('dir/*'):
    print name

print
print 'Named with explicity:'
for name in glob.glob('dir/subdir/*'):
    print name

print
print 'Named with wildchard:'
for name in glob.glob('dir/*/*'):
    print name



