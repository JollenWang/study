#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
【程序20】
 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
　　　第10次落地时，共经过多少米？第10次反弹多高？
'''

orignal = 100
rate = 1.0
sum = 0

down = 0
up = 0

for i in range(1, 11):
    down = orignal * rate
    sum += (down + up)
    rate /= 2
    up = orignal * rate

print("The 10th down tour: %f, the 10th up hight: %f" %(sum, up))


s = 100.
h = 50.0
for i in range(2, 11):
    s += 2*h
    h /= 2

print("s=%f,h=%f" %(s, h))



