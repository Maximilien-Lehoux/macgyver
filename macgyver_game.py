import random
import pygame
from pygame.locals import *


pygame.init()

window_height = 205
window_width = 300
window_size = (window_width, window_height)


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

finish = False

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

    def display_end_screen(self):
        """displays one of the two end screens according to the condition"""
        if character_macgyver.objects_number == 3:
            window.fill(pygame.Color("#EE3131"))
            window.blit(game_win.text, game_win.rectangle_text)
        else:
            window.fill(pygame.Color("#EE3131"))
            window.blit(game_over.text, game_over.rectangle_text)


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
        if event.key == K_RIGHT and character.rectangle[0] != window_width - 20:
            macgyver_location_maze[0] = character.rectangle[0] + 20
            macgyver_location_maze[1] = character.rectangle[1]
            if macgyver_location_maze not in maze:
                character.rectangle = character.rectangle.move(20, 0)

    def movement_left(self, character):
        """the character moves to the left"""
        if event.key == K_LEFT and character.rectangle[0] != 0:
            macgyver_location_maze[0] = character.rectangle[0] - 20
            macgyver_location_maze[1] = character.rectangle[1]
            if macgyver_location_maze not in maze:
                character.rectangle = character.rectangle.move(-20, 0)

    def movement_up(self, character):
        """the character moves up"""
        if event.key == K_UP and character.rectangle[1] != 0:
            macgyver_location_maze[0] = character.rectangle[0]
            macgyver_location_maze[1] = character.rectangle[1] - 20
            if macgyver_location_maze not in maze:
                character.rectangle = character.rectangle.move(0, -20)

    def movement_down(self, character):
        """the character moves down"""
        if event.key == K_DOWN and character.rectangle[1] != 160 - 20:
            macgyver_location_maze[0] = character.rectangle[0]
            macgyver_location_maze[1] = character.rectangle[1] + 20
            if macgyver_location_maze not in maze:
                character.rectangle = character.rectangle.move(0, 20)

    def random_position_object(self):
        location_object = [random.randint(0, (window_width - 20) / 10) * 10,
                           random.randint(0, (window_height - 20) / 10) * 10]
        return location_object

    def catch_object(self, object, location_score):
        """the character catches objects"""
        if character_macgyver.rectangle == object.rectangle:
            object.rectangle = location_score
            character_macgyver.objects_number += 1

    def create_syringe(self):
        """the character creates the syringe when he catches the objects and it is displayed"""
        if character_macgyver.objects_number != 3:
            window.blit(background_maze.background_picture, (0, 0))
            window.blit(object_needle.picture, object_needle.rectangle)
            window.blit(object_ether.picture, object_ether.rectangle)
            window.blit(object_plastic_tube.picture, object_plastic_tube.rectangle)
        else:
            window.blit(background_maze.background_picture, (0, 0))
            window.blit(background_rules.background_colorful, background_rules.location_background_colorful)
            object_syringe.rectangle = [140, 175]
            window.blit(object_syringe.picture, object_syringe.rectangle)

    def finish_game(self):
        """the game ends when the character is in front of the goalkeeper"""
        if character_macgyver.rectangle[:2] == face_guardian:
            variable_loop = True
            return variable_loop


# Stick maze
background_maze = BackgroundPicture("pictures/structures.png", maze_location)
window.blit(background_maze.background_picture, background_maze.location_background_picture)

# Stick background rules games
background_rules = BackgroundColor(background_rules_color, rules_location)

# Window game_over
game_over = TextGame(None, 72, "Game Over", "#FFFF00")

# Window game_win
game_win = TextGame(None, 72, "YOU WIN !!!", "#FFFF00")

# Create characters and objects
character_macgyver = Items("pictures/MacGyver.png", macgyver_location)
character_guardian = Items("pictures/Gardien.png", gardian_location)
object_needle = Items("pictures/aiguille.png", needle_location)
object_ether = Items("pictures/ether.png", ether_location)
object_plastic_tube = Items("pictures/tube_plastique.png", plastic_tube_location)
object_syringe = Items("pictures/seringue.png", syringe_location)


while not finish:
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            finish = True

        # moving character
        elif event.type == KEYDOWN:
            character_macgyver.movement_right(character_macgyver)
            character_macgyver.movement_left(character_macgyver)
            character_macgyver.movement_up(character_macgyver)
            character_macgyver.movement_down(character_macgyver)

    # the characters catches objects
    character_macgyver.catch_object(object_ether, ether_location_score)
    character_macgyver.catch_object(object_needle, needle_location_score)
    character_macgyver.catch_object(object_plastic_tube, plastic_tube_location_score)

    # the character create objects
    character_macgyver.create_syringe()

    # the game ends
    finish = character_macgyver.finish_game()

    window.blit(character_guardian.picture, character_guardian.rectangle)
    window.blit(character_macgyver.picture, character_macgyver.rectangle)
    pygame.display.flip()


# the end window is displayed
game_over.display_end_screen()

pygame.display.flip()
pygame.time.delay(5000)
pygame.display.quit()
