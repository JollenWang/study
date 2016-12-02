#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''

import datetime
import time

dtstr = str(raw_input('Enter the datetime:(YYMMDD):'))
dt = datetime.datetime.strptime(dtstr, "%Y%m%d")

another_dtstr = dtstr[:4] + "0101"
another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")

print "The date %s is the %dth day in the year!" %(dtstr, int((dt-another_dt).days + 1))






