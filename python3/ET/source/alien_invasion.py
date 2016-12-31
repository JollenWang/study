#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from status import GameStatus
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")

    ship = Ship(ai_settings, screen) 
    bullets = Group()
    aliens = Group()
    status = GameStatus(ai_settings)
    sb = Scoreboard(ai_settings, screen, status)

    gf.create_alien_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, status, sb, play_button, ship, bullets, aliens)
        gf.update_screen(ai_settings, screen, status, sb, ship, bullets, aliens, play_button)
        if status.game_active:
            ship.update()

            sb.prep_score()
            gf.update_bullets(ai_settings, status, sb, screen, ship, bullets, aliens)
            #gf.update_screen(ai_settings, screen, status, ship, bullets, aliens, play_button)
            gf.update_aliens(ai_settings, status, screen, sb, ship, aliens, bullets)

if __name__ == "__main__":
    run_game()

