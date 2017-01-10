#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	return None

