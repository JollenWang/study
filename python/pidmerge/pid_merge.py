#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/08/31
#version: 1.0
#description: Merge the PIDs by user defined.

import os.path

def get_stream():
    while True:
        stream = ''
        s = str(raw_input("$>input ts file:"))
        if s == '':
            stream = "./NSK2_Secondary_pid_new.ts"
            print "$>input null,use default file:", stream
            break;
        elif s == 'Q' or s == 'q':
            print "#>cancelled."
            break;

        if not os.path.isfile(s):
            print "#>file is not exist!, input again or press Q exit."
            continue

        path = os.path.dirname(s)
        stream = os.path.basename(s)
        if stream == '':
            print "#>invalid file,input again."
            continue
        print "%-15s: %s" %("$>path", path)
        print "%-15s: %s" %("$>stream", stream)
        break
    return stream

sfile = get_stream()
print
print "$>get stream file:", sfile



