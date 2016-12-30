#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

class Settings():
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 60, 60, 60
        self.last_fired = 0

        self.alien_speed_factor = 3
        self.fleet_drop_speed = 18
        self.fleet_direction = 1




