#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

def get_formatted_name(first, last):
    fname = first + ' ' + last
    return fname.title()

def get_long_name(first, middle, last):
    return first.title() + ' ' + middle.title() + ' ' + last.title()
