import random
import pygame
from pygame.locals import *

from structure import *

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

rules_location = [0, 165]
background_rules_color = "#EE3131"


needle_location = random.choice([[0, 140], [280, 100], [280, 40]])
ether_location = random.choice([[200, 120], [100, 120], [40, 120]])
plastic_tube_location = random.choice([[140, 60], [120, 20], [240, 40]])

ether_location_score = [40, 175]
plastic_tube_location_score = [140, 175]
needle_location_score = [240, 175]
syringe_location = [300, 350]

macgyver_location = [0, 0]
macgyver_location_maze = [0, 0]
gardian_location = [260, 0]
face_guardian = [260, 20]


class Items:
    """Create game characters and objects"""
    def __init__(self, picture, item_location):
        self.picture = pygame.image.load(picture).convert_alpha()
        self.picture = pygame.transform.scale(self.picture, (20, 20))
        self.rectangle = self.picture.get_rect()
        self.rectangle.topleft = item_location
        self.objects_number = 0
        window.blit(self.picture, self.rectangle)

    def movement_right(self, character):
        """the character moves to the right"""
        if character.rectangle[0] != window_width - 20:
            macgyver_location_maze[0] = character.rectangle[0] + 20
            macgyver_location_maze[1] = character.rectangle[1]
            if macgyver_location_maze not in maze:
                character.rectangle = character.rectangle.move(20, 0)

    def movement_left(self, character):
        """the character moves to the left"""
        if character.rectangle[0] != 0:
            macgyver_location_maze[0] = character.rectangle[0] - 20
            macgyver_location_maze[1] = character.rectangle[1]
            if macgyver_location_maze not in maze:
                character.rectangle = character.rectangle.move(-20, 0)

    def movement_up(self, character):
        """the character moves up"""
        if character.rectangle[1] != 0:
            macgyver_location_maze[0] = character.rectangle[0]
            macgyver_location_maze[1] = character.rectangle[1] - 20
            if macgyver_location_maze not in maze:
                character.rectangle = character.rectangle.move(0, -20)

    def movement_down(self, character):
        """the character moves down"""
        if character.rectangle[1] != 160 - 20:
            macgyver_location_maze[0] = character.rectangle[0]
            macgyver_location_maze[1] = character.rectangle[1] + 20
            if macgyver_location_maze not in maze:
                character.rectangle = character.rectangle.move(0, 20)

    def random_position_object(self):
        location_object = [random.randint(0, (window_width - 20) / 10) * 10,
                           random.randint(0, (window_height - 20) / 10) * 10]
        return location_object

    def catch_object(self, character, object, location_score):
        """the character catches objects"""
        if character.rectangle == object.rectangle:
            object.rectangle = location_score
            character.objects_number += 1


    def finish_game(self, character):
        """the game ends when the character is in front of the goalkeeper"""
        if character.rectangle[:2] == face_guardian:
            variable_loop = True
            return variable_loop