#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#336699', base_style = LCS)
chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
	{'value':1601, 'label':'Description of httpie'},
	{'value':2355, 'label':'Description of django'},
	{'value':1980, 'label':'Description of flask'},
]

chart.add('', plot_dicts)
chart.render_to_file('./saves/bar_descriptions.svg')

