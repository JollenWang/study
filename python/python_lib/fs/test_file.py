#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import os.path

FILENAMES = [__file__, os.path.dirname(__file__), '/', './broken_link']
for file in FILENAMES:
    print 'FILE         :', file
    print 'Absolute     :', os.path.isabs(file)
    print 'Is File?     :', os.path.isfile(file)
    print 'Is Dir?      :', os.path.isdir(file)
    print 'Is Link?     :', os.path.islink(file)
    print 'Mountpoint?  :', os.path.ismount(file)
    print 'Exists?      :', os.path.exists(file)
    print 'Link Exists? :', os.path.lexists(file)
    print
