#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import requests
from operator import itemgetter

mother_url = 'https://news.ycombinator.com/news'
r = requests.get(mother_url)
print("status code:", r.status_code)

submission_dicts = []
for id in range(30):
	break
	url = mother_url + '/item?id=' + str(id) + '.json'
	submission = requests.get(url)
	print('S_CODE:', submission.status_code)
	reponse_dict = submission.json()

	submission_dict = {
		'title' : reponse_dict['title'],
		'link'	: mother_url + '/item?id=' + str(id),
		'comments' : reponse_dict.get('descendants', 0)
	}
	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key = itemgetter('comments'), resverse = True)

for submission_dict in submission_dicts:
	print("\nTitle:", submission_dict['title'])
	print("Discussion link:", submission_dict['link'])
	print("Comments:", submission_dict['comments'])

