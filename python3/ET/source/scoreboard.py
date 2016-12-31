#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    def __init__(self, ai_settings, screen, status):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = ai_settings
        self.status = status

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_highest_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        round_score = int(round(self.status.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highest_score(self):
        round_score = int(round(self.status.highest_score, -1))
        score_str = "{:,}".format(round_score)
        self.highest_score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.right = self.screen_rect.centerx
        self.highest_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.status.level), True, 
                            self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for id in range(self.status.ship_left):
            ship = Ship(self.settings, self.screen)
            ship.image = pygame.image.load("../images/WarShip_32.png")
            ship.rect.x = 10 + id * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

