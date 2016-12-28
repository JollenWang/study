#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.settings = ai_settings
        self.image = pygame.image.load('images/WarShip_64.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.mv_left = False
        self.mv_right = False
        self.fire_active = False

    def update(self):
        if self.mv_left and self.rect.left > 0:
            self.center -= self.settings.speed_factor
        if self.mv_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

