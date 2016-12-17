#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

def combine_full_name(first, last, middle = ''):
    full_name = first.title()
    if middle:
        full_name += ' ' + middle.title()
    full_name += ' ' + last.title()
    return full_name

if __name__ == "__main__":
    print("User0's full name:", combine_full_name('john', 'hooker', 'lee'))
    print("User1's full name:", combine_full_name('jollen', 'wang'))
    print("User2's full name:", combine_full_name('Fanny', 'bill'))

