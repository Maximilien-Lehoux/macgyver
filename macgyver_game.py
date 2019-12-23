import pygame
from pygame.locals import *

pygame.init()

window_height = 300
window_width = 300

lost = False

# window creation
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)

# Stick maze
background = pygame.image.load("structures.png").convert()
window.blit(background, (0, 0))

while not lost:

    for event in pygame.event.get():
        if event.type == QUIT:
            lost = True

pygame.display.quit()



