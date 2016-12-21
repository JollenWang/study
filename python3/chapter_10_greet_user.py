#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import json

fname = "./user.json"

def get_stored_name():
    try:
        fd = open(fname, 'r')
        uname = json.load(fd)
        fd.close()
    except FileNotFoundError:
        print("-->User record not found.")
        return None
    else:
        return uname

def new_user_name():
    uname = input("-->Input your name:")
    fd = open(fname, 'w')
    json.dump(uname, fd)
    return uname

def greet_user():
    uname = get_stored_name()
    if uname:
        print("%s, nice to see you again!" %uname)
    else:
        uname = new_user_name()
        print("%s, Glad to see you!" %uname)

if __name__ == "__main__":
    greet_user()
