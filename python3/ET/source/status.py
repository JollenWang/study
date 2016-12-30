#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

class GameStatus():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_status()
        self.game_active = True

    def reset_status(self):
        self.ship_left = self.ai_settings.ship_limit

