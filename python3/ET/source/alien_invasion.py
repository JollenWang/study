#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from status import GameStatus
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen) 
    bullets = Group()
    aliens = Group()
    status = GameStatus(ai_settings)

    gf.create_alien_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if status.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_screen(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, status, screen, ship, aliens, bullets)

if __name__ == "__main__":
    run_game()

