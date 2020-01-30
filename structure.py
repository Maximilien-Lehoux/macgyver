import pygame
from pygame.locals import *

import random

sprite_size = 20

window_height = (15 * sprite_size) + 45
window_width = 15 * sprite_size
window_size = (window_width, window_height)

rules_location = [0, (sprite_size * 15) + 5]
background_rules_color = "#EE3131"

image_mur = "pictures/wall.png"


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


class Level:
    """Classe permettant de créer un niveau"""

    def __init__(self, file):
        self.file = file
        self.structure = 0

    def generate(self):
        """Method to generate the level according to the file.
        We create a general list, containing a list per line to display"""
        # Open the file
        with open(self.file, "r") as file:
            level_structure = []
            # We browse the lines of the file
            for line in file:
                level_line = []
                # We browse the sprites (letters) contained in the file
                for sprite in line:
                    # We ignore the "\ n" at the end of the line
                    if sprite != '\n':
                        # We add the sprite to the line list
                        level_line.append(sprite)
                # We add the line to the level list
                level_structure.append(level_line)
            # We save this structure
            self.structure = level_structure
            return level_structure

    def display_decor(self, window, item_arrive):
        """Method for displaying the level in function
        of the structure list returned by generate()"""
        # Loading images
        wall = pygame.image.load(image_mur).convert()

        # We browse the level list
        line_number = 0
        for line in self.structure:
            # we browse the line lists
            case_number = 0
            for sprite in line:
                # We calculate the actual position in pixels
                x = case_number * sprite_size
                y = line_number * sprite_size
                if sprite == 'm':  # m = wall
                    window.blit(wall, (x, y))
                # elif sprite == 'd':  # d = start
                    # character_location = [x, y]
                    # window.blit(character.picture, (x, y))
                elif sprite == 'g':  # a = arrive
                    window.blit(item_arrive.picture, (x, y))
                case_number += 1
            line_number += 1

    def location_start_end(self, level_structure, location_character, location_face_guardian):
        line_number = 0
        for line in level_structure:
            # we browse the line lists
            case_number = 0
            for sprite in line:
                # We calculate the actual position in pixels
                x = case_number * sprite_size
                y = line_number * sprite_size
                if sprite == 's':  # d = start
                    location_character = [x, y]
                if sprite == "e":
                    location_face_guardian = [x, y]
                case_number += 1
            line_number += 1
        return location_character, location_face_guardian


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
