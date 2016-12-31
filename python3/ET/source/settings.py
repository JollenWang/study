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
        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 60, 60, 60
        self.last_fired = 0

        self.fleet_drop_speed = 12

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 3
        self.fleet_direction = 1
        self.alien_point = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)
        print("$>curren point per alien:", self.alien_point)


