import pygame
from pygame.locals import *

pygame.init()

window_height = 160
window_width = 520

lost = False

# window creation
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)

# Stick maze
background = pygame.image.load("pictures/structures.png").convert()
window.blit(background, (0, 0))

pygame.display.flip()

while not lost:

    for event in pygame.event.get():
        if event.type == QUIT:
            lost = True

    window.blit(background, (0, 0))

pygame.display.quit()



