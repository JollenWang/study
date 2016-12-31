#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import sys
import pygame
from time import sleep
from pygame.locals import *
from bullet import Bullet
from alien import Alien
#from ship import Ship
#from settings import Settings

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

def check_play_button(ai_settings, screen, ship, bullets, aliens, status, scoreboard, button, mouse_x, mouse_y):
    clicked =  button.rect.collidepoint(mouse_x, mouse_y)
    if clicked and not status.game_active:
        ai_settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)
        status.reset_status()
        status.game_active = True

        scoreboard.prep_score()
        scoreboard.prep_highest_score()
        scoreboard.prep_level()
        scoreboard.prep_ships()

        aliens.empty()
        bullets.empty()

        create_alien_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_events(ai_settings, screen, status, scoreboard, button, ship, bullets, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down_reponse(event.key, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            key_up_reponse(event.key, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, ship, bullets, aliens, status, scoreboard, 
                                button, mouse_x, mouse_y)

def update_screen(ai_settings, screen, status, scoreboard, ship, bullets, aliens, button):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw()

    ship.blitme()
    aliens.draw(screen)

    scoreboard.show_score()
    if not status.game_active:
        button.draw_button()

    pygame.display.flip()

#
# create bullets and update them in screen
#
def remove_disappered_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print("bullets:%d", len(bullets))

def fire_bullet(ai_settings, screen, ship, bullets):
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)
    last_bullet = new_bullet


def check_highest_score(status, scoreboard):
    if status.score >= status.highest_score:
        status.highest_score = status.score
        scoreboard.prep_highest_score()

def check_bullet_alien_collisions(ai_settings, status, scoreboard, screen, ship, bullets, aliens):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            status.score += ai_settings.alien_point
            scoreboard.prep_score()
        check_highest_score(status, scoreboard)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()

        status.level += 1
        scoreboard.prep_level()

        create_alien_fleet(ai_settings, screen, ship, aliens)

def update_bullets(ai_settings, status, scoreboard, screen, ship, bullets, aliens):
    if ship.fire_active:
        ai_settings.last_fired += ai_settings.bullet_speed_factor
        if ai_settings.last_fired >= ai_settings.bullet_height * 2:
            fire_bullet(ai_settings, screen, ship, bullets)
            ai_settings.last_fired = 0

    bullets.update()
    remove_disappered_bullets(bullets)
    check_bullet_alien_collisions(ai_settings, status, scoreboard, screen, ship, bullets, aliens)
#
# create alien fleet and store in aliens
#
def get_alien_rows_number(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - (2 * alien_height + ship_height)
    return int(available_space_y / (2 * alien_height))

def get_alien_number_per_line(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    return int(available_space_x / (2 * alien_width))

def create_alien_by_id(ai_settings, screen, aliens, alien_id, row_id):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_id
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_id
    aliens.add(alien)

def create_alien_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    alien_numbers = get_alien_number_per_line(ai_settings, alien.rect.width)
    rows_number = get_alien_rows_number(ai_settings, ship.rect.height, alien.rect.height)

    #print("$>create %d line * %d group aliens" %(rows_number, alien_numbers))
    for row_id in range(rows_number):
        for alien_id in range(alien_numbers):
            create_alien_by_id(ai_settings, screen, aliens, alien_id, row_id)


def ship_hit(ai_settings, status, screen, scoreboard, ship, aliens, bullets):
    status.ship_left -= 1
    ai_settings.initialize_dynamic_settings()

    if status.ship_left > 0:
        print("#>ship destoried, play again!!!")
        status.score = 0
        scoreboard.prep_score()
        scoreboard.prep_ships()

        aliens.empty()
        bullets.empty()
        create_alien_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(1)
    else:
        print("!!!Game Over!!!")
        status.game_active = False
        pygame.mouse.set_visible(True)

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def check_aliens_bottom(ai_settings, status, screen, scoreboard, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, status, screen, scoreboard, ship, aliens, bullets)
            break

def update_aliens(ai_settings, status, screen, scoreboard, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, status, screen, scoreboard, ship, aliens, bullets)
    else:
        check_aliens_bottom(ai_settings, status, screen, scoreboard, ship, aliens, bullets)
