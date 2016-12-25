#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import func_random_param

print(__name__)

if __name__ == "__main__":
    pf = func_random_param.build_profile('Jollen', 'Wang', age = '24', school = 'MIT')
    print(pf)

