#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

import os.path

for path in ['filename.txt',
             'filename',
             '/1/2/filename.txt',
             '/',
             '',
             'my-archive.tar.gz',
             'no-extension.',
            ]:
    print '%21s :' %path, os.path.splitext(path)
