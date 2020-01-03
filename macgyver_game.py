import pygame
from pygame.locals import *
import random

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


needle_location = [[0, 140], [280, 100], [280, 40]]
ether_location = [[200, 120], [100, 120], [40, 120]]
plastic_tube_location = [[140, 60], [120, 20], [240, 40]]
syringe_location = []

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


character_guardian = pygame.image.load("pictures/Gardien.png").convert_alpha()
character_guardian = pygame.transform.scale(character_guardian, (20, 20))
character_guardian_rect = character_guardian.get_rect()
character_guardian_rect.topleft = [260, 0]
window.blit(character_guardian, character_guardian_rect)

# create objects and rectangles
object_needle = pygame.image.load("pictures/aiguille.png").convert_alpha()
object_needle = pygame.transform.scale(object_needle, (20, 20))
object_needle_rect = object_needle.get_rect()
object_needle_rect.topleft = random.choice(needle_location)
window.blit(object_needle, object_needle_rect)

object_ether = pygame.image.load("pictures/ether.png").convert_alpha()
object_ether = pygame.transform.scale(object_ether, (20, 20))
object_ether_rect = object_ether.get_rect()
object_ether_rect.topleft = random.choice(ether_location)
window.blit(object_ether, object_ether_rect)

object_plastic_tube = pygame.image.load("pictures/tube_plastique.png").convert_alpha()
object_plastic_tube = pygame.transform.scale(object_plastic_tube, (20, 20))
object_plastic_tube_rect = object_plastic_tube.get_rect()
object_plastic_tube_rect.topleft = random.choice(plastic_tube_location)
window.blit(object_plastic_tube, object_plastic_tube_rect)

object_syringe = pygame.image.load("pictures/seringue.png").convert_alpha()
object_syringe = pygame.transform.scale(object_syringe, (20, 20))
object_syringe_rect = object_syringe.get_rect()
object_syringe_rect.topleft = [140, 175]

macgyver_location_maze = [0, 0]
face_guardian = [260, 20]

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

class Characters:

    def __init__(self, picture):
        self.picture = pygame.image.load(picture).convert_alpha()
        self.picture = pygame.transform.scale(self.picture, (20, 20))
        self.rectangle = self.picture.get_rect()
        self.rectangle.topleft = [0, 0]
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


character_macgyver = Characters("pictures/MacGyver.png")

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

    if character_macgyver.rectangle == object_ether_rect:
        object_ether_rect = [40, 175]
        objects_numbers += 1

    if character_macgyver.rectangle == object_needle_rect:
        object_needle_rect = [240, 175]
        objects_numbers += 1

    if character_macgyver.rectangle == object_plastic_tube_rect:
        object_plastic_tube_rect = [140, 175]
        objects_numbers += 1

    if objects_numbers != 3:
        window.blit(background, (0, 0))
        window.blit(object_needle, object_needle_rect)
        window.blit(object_ether, object_ether_rect)
        window.blit(object_plastic_tube, object_plastic_tube_rect)
    else:
        window.blit(background, (0, 0))
        window.blit(background_rules, (0, 165))
        window.blit(object_syringe, object_syringe_rect)

    if character_macgyver.rectangle[:2] == face_guardian:
        lost = True

    window.blit(character_guardian, character_guardian_rect)
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
