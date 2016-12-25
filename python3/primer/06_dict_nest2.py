#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
    },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris'
    },
}

for uname, uinfo in users.items():
    print("User name: " + uname.title())
    print("\tFull name: " + uinfo['first'].title() + " " + uinfo['last'].title())
    print("\tLocation: " + uinfo['location'].title())
