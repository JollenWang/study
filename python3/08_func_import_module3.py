#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

from func_random_param import build_profile as bp

print(__name__)
if __name__ == "__main__":
    pf = bp('Jollen', 'Wang', age = '24', school = 'MIT')
    print(pf)

