#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates, highs = [], []
	for row in reader:
		current_date = datetime.strptime(row[0], "%Y-%m-%d")
		dates.append(current_date)
		highs.append(int(row[1]))
	print(highs)

	fig = plt.figure(dpi = 128, figsize = (10, 6))
	plt.plot(dates, highs, c = 'red')
	plt.title('Daily high temperatures, July 2014', fontsize = 24)
	plt.xlabel('', fontsize = 16)
	fig.autofmt_xdate()

	plt.ylabel('Temperature (F)', fontsize = 16)
	plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

	plt.savefig('./saves/sitka_weathter-07-2014.png', bbox_inches = 'tight')
	plt.show()

