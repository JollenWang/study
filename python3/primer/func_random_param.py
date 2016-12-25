#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

def build_profile(first, last, **usr_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in usr_info.items():
        profile[k] = v
    return profile

if __name__ == "__main__":
    pf = build_profile('Albert', 'Einstein', location = 'Princeton', filed = 'Physics')
    print(pf)
