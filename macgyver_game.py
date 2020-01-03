import random
import pygame
from pygame.locals import *

from classes import *

pygame.init()

window_height = 205
window_width = 300

maze = [[140, 0], [160, 0], [180, 0], [200, 0], [220, 0], [240, 0], [280, 0],
        [20, 20], [40, 20], [60, 20], [80, 20], [140, 20], [160, 20], [180, 20], [200, 20], [220, 20], [240, 20],
        [20, 40], [80, 40], [120, 40], [140, 40], [200, 40], [220, 40],
        [20, 60], [80, 60], [160, 60], [180, 60], [200, 60], [220, 60], [280, 60],
        [20, 80], [40, 80], [60, 80], [80, 80],

        [60, 120], [80, 120], [120, 120], [140, 120], [160, 120], [180, 120], [220, 120], [240, 120], [260, 120],
        [280, 120],

        [40, 140], [60, 140], [80, 140], [100, 140], [140, 140], [160, 140], [200, 140], [220, 140], [260, 140],
        [280, 140]]


needle_location = random.choice([[0, 140], [280, 100], [280, 40]])
ether_location = random.choice([[200, 120], [100, 120], [40, 120]])
plastic_tube_location = random.choice([[140, 60], [120, 20], [240, 40]])
syringe_location = [300, 350]

macgyver_location = [0, 0]
macgyver_location_maze = [0, 0]
gardian_location = [260, 0]
face_guardian = [260, 20]

objects_numbers = 0

lost = False

# window creation
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)

# Stick maze
background = pygame.image.load("pictures/structures.png").convert_alpha()
window.blit(background, (0, 0))

# Stick background rules games
background_rules = pygame.Surface(window.get_size())
background_rules = background_rules.convert()
background_rules.fill(pygame.Color("#EE3131"))
window.blit(background_rules, (0, 165))


# Screen window_end
rect_window_end = window.get_rect()
police_game_end = pygame.font.Font(None, 72)

# Window game_over
text_game_over = police_game_end.render("Game Over", True, pygame.Color("#FFFF00"))
square_text_game_over = text_game_over.get_rect()
square_text_game_over.center = rect_window_end.center

# Window game_win
text_game_win = police_game_end.render("YOU WIN !!!", True, pygame.Color("#FFFF00"))
square_text_game_win = text_game_win.get_rect()
square_text_game_win.center = rect_window_end.center

# class and method


class Items:

    def __init__(self, picture, item_location):
        self.picture = pygame.image.load(picture).convert_alpha()
        self.picture = pygame.transform.scale(self.picture, (20, 20))
        self.rectangle = self.picture.get_rect()
        self.rectangle.topleft = item_location
        window.blit(self.picture, self.rectangle)

    def movement_right(self, character):
        if event.key == K_RIGHT and character.rectangle[0] != window_width - 20:
            macgyver_location_maze[0] = character.rectangle[0] + 20
            macgyver_location_maze[1] = character.rectangle[1]
            if macgyver_location_maze not in maze:
                character.rectangle = character.rectangle.move(20, 0)

    def movement_left(self, character):
        if event.key == K_LEFT and character.rectangle[0] != 0:
            macgyver_location_maze[0] = character.rectangle[0] - 20
            macgyver_location_maze[1] = character.rectangle[1]
            if macgyver_location_maze not in maze:
                character.rectangle = character.rectangle.move(-20, 0)

    def movement_up(self, character):
        if event.key == K_UP and character.rectangle[1] != 0:
            macgyver_location_maze[0] = character.rectangle[0]
            macgyver_location_maze[1] = character.rectangle[1] - 20
            if macgyver_location_maze not in maze:
                character.rectangle = character.rectangle.move(0, -20)

    def movement_down(self, character):
        if event.key == K_DOWN and character.rectangle[1] != 160 - 20:
            macgyver_location_maze[0] = character.rectangle[0]
            macgyver_location_maze[1] = character.rectangle[1] + 20
            if macgyver_location_maze not in maze:
                character.rectangle = character.rectangle.move(0, 20)


# Create items
character_macgyver = Items("pictures/MacGyver.png", macgyver_location)
character_guardian = Items("pictures/Gardien.png", gardian_location)
object_needle = Items("pictures/aiguille.png", needle_location)
object_ether = Items("pictures/ether.png", ether_location)
object_plastic_tube = Items("pictures/tube_plastique.png", plastic_tube_location)
object_syringe = Items("pictures/seringue.png", syringe_location)


while not lost:
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            lost = True

        elif event.type == KEYDOWN:  # and character_macgyver_rect[:2] not in maze:
            character_macgyver.movement_right(character_macgyver)
            character_macgyver.movement_left(character_macgyver)
            character_macgyver.movement_up(character_macgyver)
            character_macgyver.movement_down(character_macgyver)

    if character_macgyver.rectangle == object_ether.rectangle:
        object_ether.rectangle = [40, 175]
        objects_numbers += 1

    if character_macgyver.rectangle == object_needle.rectangle:
        object_needle.rectangle = [240, 175]
        objects_numbers += 1

    if character_macgyver.rectangle == object_plastic_tube.rectangle:
        object_plastic_tube.rectangle = [140, 175]
        objects_numbers += 1

    if objects_numbers != 3:
        window.blit(background, (0, 0))
        window.blit(object_needle.picture, object_needle.rectangle)
        window.blit(object_ether.picture, object_ether.rectangle)
        window.blit(object_plastic_tube.picture, object_plastic_tube.rectangle)
    else:
        window.blit(background, (0, 0))
        window.blit(background_rules, (0, 165))
        object_syringe.rectangle = [140, 175]
        window.blit(object_syringe.picture, object_syringe.rectangle)

    if character_macgyver.rectangle[:2] == face_guardian:
        lost = True

    window.blit(character_guardian.picture, character_guardian.rectangle)
    window.blit(character_macgyver.picture, character_macgyver.rectangle)

    pygame.display.flip()

if objects_numbers == 3:
    window.fill(pygame.Color("#EE3131"))
    window.blit(text_game_win, square_text_game_win)
else:
    window.fill(pygame.Color("#EE3131"))
    window.blit(text_game_over, square_text_game_over)
    
pygame.display.flip()
pygame.time.delay(5000)
pygame.display.quit()
