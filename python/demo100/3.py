#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
# 第三题：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少
'''
import math

num=0
while True:
	if math.sqrt(num+100) == int(math.sqrt(num+100)) and math.sqrt(num+168) == int(math.sqrt(num+168)):
		print"Find:", num
		break
	num+=1

#--------------------------------------------------------
def chk_full_sqrt(num, base):
	tmp=num+base
	if math.sqrt(tmp) == int(math.sqrt(tmp)):
		return True
	else:
		return False

def find_num():
	n=0
	while True:
		if chk_full_sqrt(n, 100) and chk_full_sqrt(n, 168):
			print "Get the num1:", n
			break
		n+=1

find_num()

n=0
while True:
	if chk_full_sqrt(n, 100) and chk_full_sqrt(n, 168):
		print "Get the num2:", n
		break
	n+=1
