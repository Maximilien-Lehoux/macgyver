from structure import *

rules_location = [0, 165]
background_rules_color = "#EE3131"

needle_location = [0, 140]
ether_location = [100, 120]
plastic_tube_location = [140, 60]

ether_location_score = [40, 315]
plastic_tube_location_score = [140, 315]
needle_location_score = [240, 315]
syringe_location = [300, 350]

macgyver_location = [150, 150]
macgyver_location_maze = [0, 0]
gardian_location = [260, 0]
face_guardian = [260, 20]


class Items:
    """Create objects and guardian"""
    def __init__(self, picture, item_location):
        self.picture = pygame.image.load(picture).convert_alpha()
        self.picture = pygame.transform.scale(self.picture, (sprite_size, sprite_size))
        self.rectangle = self.picture.get_rect()
        self.rectangle.topleft = item_location
        self.objects_number = 0
        window.blit(self.picture, self.rectangle)

    def random_object(self, level_structure):
        number_line = 1
        number_column = 1
        while level_structure[number_line][number_column] == 'm' \
                or level_structure[number_line][number_column] == 'd'\
                or level_structure[number_line][number_column] == 'a':
            number_line = random.randint(0, 14)
            number_column = random.randint(0, 14)
        object_location = [number_column * sprite_size, number_line * sprite_size]
        return object_location


class Characters:
    def __init__(self, picture, item_location):
        self.picture = pygame.image.load(picture).convert_alpha()
        self.picture = pygame.transform.scale(self.picture, (sprite_size, sprite_size))
        self.rectangle = self.picture.get_rect()
        self.rectangle.topleft = item_location
        self.objects_number = 0
        window.blit(self.picture, self.rectangle)

    def movement_right(self, character, level_structure):
        """the character moves to the right"""
        if character.rectangle[0] != window_width - sprite_size:
            macgyver_location_maze[0] = int((character.rectangle[0] + sprite_size) / sprite_size)
            macgyver_location_maze[1] = int((character.rectangle[1]) / sprite_size)
            if level_structure[macgyver_location_maze[1]][macgyver_location_maze[0]] != 'm':
                character.rectangle = character.rectangle.move(sprite_size, 0)

    def movement_left(self, character, level_structure):
        """the character moves to the left"""
        if character.rectangle[0] != 0:
            macgyver_location_maze[0] = int((character.rectangle[0] - sprite_size) / sprite_size)
            macgyver_location_maze[1] = int((character.rectangle[1]) / sprite_size)
            if level_structure[macgyver_location_maze[1]][macgyver_location_maze[0]] != 'm':
                character.rectangle = character.rectangle.move(-sprite_size, 0)

    def movement_up(self, character, level_structure):
        """the character moves up"""
        if character.rectangle[1] != 0:
            macgyver_location_maze[0] = int((character.rectangle[0]) / sprite_size)
            macgyver_location_maze[1] = int((character.rectangle[1] - sprite_size) / sprite_size)
            if level_structure[macgyver_location_maze[1]][macgyver_location_maze[0]] != 'm':
                character.rectangle = character.rectangle.move(0, -sprite_size)

    def movement_down(self, character, level_structure):
        """the character moves down"""
        if character.rectangle[1] != 300 - sprite_size:
            macgyver_location_maze[0] = int((character.rectangle[0]) / sprite_size)
            macgyver_location_maze[1] = int((character.rectangle[1] + sprite_size) / sprite_size)
            if level_structure[macgyver_location_maze[1]][macgyver_location_maze[0]] != 'm':
                character.rectangle = character.rectangle.move(0, sprite_size)

    def catch_object(self, character, object, location_score):
        """the character catches objects"""
        if character.rectangle[:2] == object.rectangle:
            object.rectangle = location_score
            character.objects_number += 1

    def finish_game(self, character, case_end):
        """the game ends when the character is in front of the goalkeeper"""
        if character.rectangle[:2] == case_end:
            variable_loop = True
            return variable_loop