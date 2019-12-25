import pygame
from pygame.locals import *

pygame.init()

window_height = 160
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

# needle_location = []



lost = False

# window creation
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)

# Stick maze
background = pygame.image.load("pictures/structures.png").convert_alpha()
window.blit(background, (0, 0))

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
object_needle_rect.topleft = (100, 0)
window.blit(object_needle, object_needle_rect)

object_ether_rect = object_ether.get_rect()
object_ether_rect.topleft = (100, 60)
window.blit(object_ether, object_ether_rect)

object_plastic_tube_rect = object_plastic_tube.get_rect()
object_plastic_tube_rect.topleft = (100, 80)
window.blit(object_plastic_tube, object_plastic_tube_rect)


while not lost:

    for event in pygame.event.get():
        if event.type == QUIT:
            lost = True

    pygame.display.flip()

pygame.display.quit()



