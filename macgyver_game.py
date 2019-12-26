import pygame
from pygame.locals import *
import random
import fonctions

pygame.init()

window_height = 205
window_width = 300

maze = [[140, 0], [160, 0], [180, 0], [200, 0], [220, 0], [240, 0], [280, 0],
        [20, 20], [40, 20], [60, 20], [80, 20], [140, 20], [160, 20], [180, 20], [200, 20], [220, 20], [240, 20],
        [20, 40], [80, 40], [120, 40], [140, 40], [200, 40], [220, 40],
        [20, 60], [80, 60], [160, 60], [180, 60], [200, 60], [220, 60], [280, 60],
        [20, 80], [40, 80], [60, 80], [80, 80],

        [80, 120], [120, 120], [140, 120], [160, 120], [180, 120], [220, 120], [240, 120], [260, 120],
        [280, 120],

        [40, 140], [60, 140], [80, 140], [100, 140], [140, 140], [160, 140], [200, 140], [220, 140], [260, 140],
        [280, 140]]


needle_location = [[0, 140], [280, 100], [280, 40]]
ether_location = [[200, 120], [100, 120], [60, 120]]
plastic_tube_location = [[140, 60], [120, 20], [240, 40]]

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
background_rules.fill(pygame.Color("#575757"))
window.blit(background_rules, (0, 165))

# create characters
character_macgyver = pygame.image.load("pictures/MacGyver.png").convert_alpha()
character_macgyver = pygame.transform.scale(character_macgyver, (20, 20))

character_guardian = pygame.image.load("pictures/Gardien.png").convert_alpha()
character_guardian = pygame.transform.scale(character_guardian, (20, 20))

# create objects
object_needle = pygame.image.load("pictures/aiguille.png").convert_alpha()
object_needle = pygame.transform.scale(object_needle, (20, 20))

object_ether = pygame.image.load("pictures/ether.png").convert_alpha()
object_ether = pygame.transform.scale(object_ether, (20, 20))

object_plastic_tube = pygame.image.load("pictures/tube_plastique.png").convert_alpha()
object_plastic_tube = pygame.transform.scale(object_plastic_tube, (20, 20))

# Create rectangles characters
character_macgyver_rect = character_macgyver.get_rect()
character_macgyver_rect.topleft = (0, 0)
window.blit(character_macgyver, character_macgyver_rect)

character_guardian_rect = character_guardian.get_rect()
character_guardian_rect.topleft = (260, 0)
window.blit(character_guardian, character_guardian_rect)

# Create rectangles objects
object_needle_rect = object_needle.get_rect()
object_needle_rect.topleft = random.choice(needle_location)
window.blit(object_needle, object_needle_rect)

object_ether_rect = object_ether.get_rect()
object_ether_rect.topleft = random.choice(ether_location)
window.blit(object_ether, object_ether_rect)

object_plastic_tube_rect = object_plastic_tube.get_rect()
object_plastic_tube_rect.topleft = random.choice(plastic_tube_location)
window.blit(object_plastic_tube, object_plastic_tube_rect)

macgyver_location_maze = [0, 0]
face_guardian = [260, 20]

while not lost:
    pygame.time.Clock().tick(30)

    if character_macgyver_rect[:2] == face_guardian and objects_numbers != 3:
        lost = True

    for event in pygame.event.get():
        if event.type == QUIT:
            lost = True

        elif event.type == KEYDOWN:  # and character_macgyver_rect[:2] not in maze:
            if event.key == K_DOWN and character_macgyver_rect[1] != 160 - 20:
                macgyver_location_maze[0] = character_macgyver_rect[0]
                macgyver_location_maze[1] = character_macgyver_rect[1] + 20
                if macgyver_location_maze not in maze:
                    character_macgyver_rect = character_macgyver_rect.move(0, 20)

            if event.key == K_RIGHT and character_macgyver_rect[0] != window_width - 20:
                macgyver_location_maze[0] = character_macgyver_rect[0] + 20
                macgyver_location_maze[1] = character_macgyver_rect[1]
                if macgyver_location_maze not in maze:
                    character_macgyver_rect = character_macgyver_rect.move(20, 0)

            if event.key == K_LEFT and character_macgyver_rect[0] != 0:
                macgyver_location_maze[0] = character_macgyver_rect[0] - 20
                macgyver_location_maze[1] = character_macgyver_rect[1]
                if macgyver_location_maze not in maze:
                    character_macgyver_rect = character_macgyver_rect.move(-20, 0)

            if event.key == K_UP and character_macgyver_rect[1] != 0:
                macgyver_location_maze[0] = character_macgyver_rect[0]
                macgyver_location_maze[1] = character_macgyver_rect[1] - 20
                if macgyver_location_maze not in maze:
                    character_macgyver_rect = character_macgyver_rect.move(0, -20)

    window.blit(background, (0, 0))
    window.blit(character_guardian, character_guardian_rect)
    window.blit(object_needle, object_needle_rect)
    window.blit(object_ether, object_ether_rect)
    window.blit(object_plastic_tube, object_plastic_tube_rect)
    window.blit(character_macgyver, character_macgyver_rect)

    pygame.display.flip()



pygame.display.quit()
