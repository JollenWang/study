#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=python&sort=stars'
r = requests.get(url)

print('Status code', r.status_code)

response_dict = r.json()
print(response_dict.keys())
print("Total Respositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print("Respositories returned:", len(repo_dicts))

#research the first repository
repo_dict = repo_dicts[0]
print('\nKeys:', len(repo_dict))
#for key in sorted(repo_dict.keys()):
#	print(key)

print('\nSelected infomation of each repository')
names, stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])
#	print('\nName:', repo_dict['name'])
#	print('Owner:', repo_dict['owner']['login'])
#	print('Stars:', repo_dict['stargazers_count'])
#	print('Repository:', repo_dict['html_url'])
#	print('Created:', repo_dict['created_at'])
#	print('Update:', repo_dict['updated_at'])
#	print('Description:', repo_dict['description'])

my_style = LS('#336699', base_style = LCS)
my_cfg = pygal.Config()
my_cfg.x_label_rotation = 45
my_cfg.show_legend = False
my_cfg.title_font_size = 24
my_cfg.label_font_size = 15
my_cfg.major_label_font_size = 18
my_cfg.truncate_label = 15
my_cfg.show_y_guides = False
my_cfg.width = 1000

chart = pygal.Bar(my_cfg, style = my_style)
chart.title = 'Most Popular Python Projects on Github'
chart.x_labels = names

chart.add('Star', stars)
chart.render_to_file("./saves/python_repository.svg")


