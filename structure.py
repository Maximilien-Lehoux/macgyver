import pygame
from pygame.locals import *

import random

maze = [[140, 0], [160, 0], [180, 0], [200, 0], [220, 0], [240, 0], [280, 0],
        [20, 20], [40, 20], [60, 20], [80, 20], [140, 20], [160, 20], [180, 20], [200, 20], [220, 20], [240, 20],
        [20, 40], [80, 40], [120, 40], [140, 40], [200, 40], [220, 40],
        [20, 60], [80, 60], [160, 60], [180, 60], [200, 60], [220, 60], [280, 60],
        [20, 80], [40, 80], [60, 80], [80, 80],

        [60, 120], [80, 120], [120, 120], [140, 120], [160, 120], [180, 120], [220, 120], [240, 120], [260, 120],
        [280, 120],

        [40, 140], [60, 140], [80, 140], [100, 140], [140, 140], [160, 140], [200, 140], [220, 140], [260, 140],
        [280, 140]]

maze_location = [0, 0]

window_height = 205
window_width = 300
window_size = (window_width, window_height)

rules_location = [0, 165]
background_rules_color = "#EE3131"

window = pygame.display.set_mode(window_size)
rectangle_window = window.get_rect()


class BackgroundPicture:
    """create background from saved image"""
    def __init__(self, background, location_background_picture):
        self.background_picture = pygame.image.load(background).convert_alpha()
        self.location_background_picture = location_background_picture


class BackgroundColor:
    """create background colorful"""
    def __init__(self, background_color, location_background_colorful):
        self.background_colorful = pygame.Surface(window.get_size())
        self.background_colorful = self.background_colorful.convert()
        self.background_colorful.fill(pygame.Color(background_color))
        self.location_background_colorful = location_background_colorful
        window.blit(self.background_colorful, self.location_background_colorful)


class TextGame:
    """create game texts"""
    def __init__(self, type_police, size_police, text, color_text):
        self.police = pygame.font.Font(type_police, size_police)
        self.text = self.police.render(text, True, pygame.Color(color_text))
        self.rectangle_text = self.text.get_rect()
        self.rectangle_text.center = rectangle_window.center

    def display_end_screen(self, character, text_win, text_over):
        """displays one of the two end screens according to the condition"""
        if character.objects_number == 3:
            window.fill(pygame.Color("#EE3131"))
            window.blit(text_win.text, text_win.rectangle_text)
        else:
            window.fill(pygame.Color("#EE3131"))
            window.blit(text_over.text, text_over.rectangle_text)
