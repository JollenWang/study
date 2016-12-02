#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

#Filename:002.py

i = int(raw_input('Enter the profit:'))
arr = [1000000, 600000, 400000, 200000, 100000,0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
	this = (i - arr[idx]) * rat[idx]
        r += this
        print("$>this=", this)
        i=arr[idx]

print("$>Total:", r)
