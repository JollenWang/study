#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import json
import pygal
from country_codes import get_country_code
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

fname = "population.json"
with open(fname) as f:
	pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country)
		if code:
			cc_populations[code] = population

cc_pop0, cc_pop1, cc_pop2 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pop0[cc] = pop
	elif pop < 1000000000:
		cc_pop1[cc] = pop
	else:
		cc_pop2[cc] = pop
print(len(cc_pop0), len(cc_pop1), len(cc_pop2))

wm_style = RotateStyle('#336699', base_style = LightColorizedStyle)
#wm_style = LightColorizedStyle
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0~10m', cc_pop0)
wm.add('10m~1bn', cc_pop1)
wm.add('>1bn', cc_pop2)
wm.render_to_file('./saves/2010_world_population_figure.svg')
