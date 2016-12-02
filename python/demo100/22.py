#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定
比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出
三队赛手的名单。 
'''

for i in range(ord('x'), ord('z') + 1):
    for j in range(ord('x'), ord('z') + 1):
        if j != i:
            for k in range(ord('x'), ord('z') + 1):
                if k !=j and k != i:
                    if i != ord('x') and (k != ord('x') and k != ord('z')):
                        print("a-->%s,b-->%s,c-->%s" %(chr(i), chr(j), chr(k)))


