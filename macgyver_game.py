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



lost = False

# window creation
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)

# Stick maze
background = pygame.image.load("pictures/structures.png").convert_alpha()
window.blit(background, (0, 0))

# Stick characters
character_macgyver = pygame.image.load("pictures/MacGyver.png")
character_macgyver = pygame.transform.scale(character_macgyver, (20, 20))

character_guardian = pygame.image.load("pictures/Gardien.png").convert_alpha()
character_guardian = pygame.transform.scale (character_guardian, (20,20))


# Create rectangles
character_macgyver_rect = character_macgyver.get_rect()
character_macgyver_rect.topleft = (0, 0)
window.blit(character_macgyver, character_macgyver_rect)

character_guardian_rect = character_guardian.get_rect()
character_guardian_rect.topleft = (260, 0)
window.blit(character_guardian, character_guardian_rect)


while not lost:

    for event in pygame.event.get():
        if event.type == QUIT:
            lost = True

    pygame.display.flip()

pygame.display.quit()



