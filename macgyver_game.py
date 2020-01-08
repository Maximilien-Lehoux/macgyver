from items import *
from structure import *

pygame.init()

finish = False

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
            pygame.display.quit()

        # moving character
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                character_macgyver.movement_right(character_macgyver)
            if event.key == K_LEFT:
                character_macgyver.movement_left(character_macgyver)
            if event.key == K_UP:
                character_macgyver.movement_up(character_macgyver)
            if event.key == K_DOWN:
                character_macgyver.movement_down(character_macgyver)

    # the characters catches objects
    character_macgyver.catch_object(character_macgyver, object_ether, ether_location_score)
    character_macgyver.catch_object(character_macgyver, object_needle, needle_location_score)
    character_macgyver.catch_object(character_macgyver, object_plastic_tube, plastic_tube_location_score)

    # the character creates the syringe when he catches the objects and it is displayed
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

    # the game ends
    finish = character_macgyver.finish_game(character_macgyver)

    window.blit(character_guardian.picture, character_guardian.rectangle)
    window.blit(character_macgyver.picture, character_macgyver.rectangle)
    pygame.display.flip()


# the end window is displayed
game_over.display_end_screen(character_macgyver, game_win, game_over)

pygame.display.flip()
pygame.time.delay(5000)
pygame.display.quit()
