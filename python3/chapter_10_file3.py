#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

with open("pi.txt") as fd:
    lines = fd.readlines()
    for line in lines:
        print(line.rstrip())
