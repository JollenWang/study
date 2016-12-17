#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

src = ["Abc", "Book", "candy", "apple", "Good"]
dst = []
dst2 = []
print("Before copy:\nsrc=%s\ndst=%s" %(str(src), str(dst)))

dst = src
dst2 = dst[:]
print("After copy:\nsrc=%s\ndst=%s" %(str(src), str(dst)))
print("dst2= ", str(dst2))

print("\nsrc apped an item: ", "news")
src.append("news")
print("src new: " + str(src))
print("dst: " + str(dst))
print("dst2: " + str(dst2))
