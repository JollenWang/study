#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

src = ['abc', 'Nor', 'terry', 'King']
dst = []

def copy_to_dest(src, dst):
    print(__name__)
    while src:
        cur = src.pop()
        print('>process ' + cur)
        dst.append(cur)


if __name__ == "__main__":
    print('src0= ' + str(src))
    print('dst0= ' + str(dst))
    copy_to_dest(src[:], dst)
    print('src1= ' + str(src))
    print('dst1= ' + str(dst))
    copy_to_dest(src, dst)
    print('src2= ' + str(src))
    print('dst2= ' + str(dst))
