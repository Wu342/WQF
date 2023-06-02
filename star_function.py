import pygame
from star import Star
from random import randint
import sys

def star_column_num(settings,star_width):
    available_space_x = settings.screen_width - (2 * star_width)
    star_column_nums = int(available_space_x / (2 * star_width))
    return star_column_nums

def star_row_num(settings,star_height):
    available_space_y = settings.screen_height - (2 * star_height)
    star_row_nums = int(available_space_y / (2 * star_height))
    return star_row_nums

def create_star(settings,screen,num_star_row,num_star_column,stars):
    star = Star(settings,screen)
    star.rect.x = star.rect.width + 2 * num_star_column * star.rect.width
    star.rect.y = star.rect.height + 2 * num_star_row * star.rect.height
    stars.add(star)

def crete_stars_list(settings,screen,stars):
    star = Star(settings,screen)
    star_column_nums = star_column_num(settings,star.rect.width)
    star_row_nums = star_row_num(settings,star.rect.height)
    for num_row in range(star_row_nums):
        num_column = randint(0,star_column_nums)
        create_star(settings,screen,num_row,num_column,stars)

def update_screen(screen,star_settings,stars):
    screen.fill(star_settings.bg_color)
    crete_stars_list(star_settings, screen, stars)
    stars.draw(screen)
    pygame.display.flip()
    stars.empty()
    
def check_exit(event):
    if event.type == pygame.QUIT:
        sys.exit()
