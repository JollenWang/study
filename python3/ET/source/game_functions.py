#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import sys
import pygame
from pygame.locals import *
from bullet import Bullet
#from ship import Ship
#from settings import Settings

def fire_bullet(ai_settings, screen, ship, bullets):
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)

def key_up_reponse(key, ship):
    if key == pygame.K_LEFT:
        ship.mv_left = False
    elif key == pygame.K_RIGHT:
        ship.mv_right = False
    elif key == K_SPACE: 
        ship.fire_active = False

def key_down_reponse(key, ship, ai_settings, screen, bullets):
    if key == pygame.K_LEFT:
        ship.mv_left = True
    elif key == pygame.K_RIGHT:
        ship.mv_right = True
    elif key == K_q:
        sys.exit()
    elif key == K_SPACE:
        ship.fire_active = True
        #fire_bullet(ai_settings, screen, ship, bullets)

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down_reponse(event.key, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            key_up_reponse(event.key, ship)

def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw()

    ship.blitme()
    pygame.display.flip()

def remove_disappered_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print("bullets:%d", len(bullets))

def update_bullets(ai_settings, screen, ship, bullets):
    if ship.fire_active:
        fire_bullet(ai_settings, screen, ship, bullets)
    bullets.update()
    remove_disappered_bullets(bullets)

