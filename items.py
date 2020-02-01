from structure import *

needle_location = [0, 0]
ether_location = [0, 0]
plastic_tube_location = [0, 0]

ether_location_score = [40, (15 * SPRITE_SIZE) + SPRITE_SIZE / 2]
plastic_tube_location_score = [140, (15 * SPRITE_SIZE) + SPRITE_SIZE / 2]
needle_location_score = [240, 15 * SPRITE_SIZE + SPRITE_SIZE / 2]
syringe_location = [0, 0]

macgyver_location = [0, 0]
macgyver_location_maze = [0, 0]
gardian_location = [0, 0]
face_guardian = [0, 0]


class Items:
    """Create objects and guardian"""
    def __init__(self, picture, item_location):
        self.picture = pygame.image.load(picture).convert_alpha()
        self.picture = pygame.transform.scale(self.picture, (SPRITE_SIZE, SPRITE_SIZE))
        self.rectangle = self.picture.get_rect()
        self.rectangle.topleft = item_location
        self.objects_number = 0
        window.blit(self.picture, self.rectangle)

    def random_object(self, level_structure):
        """Objects are placed randomly in the maze"""
        number_line = 1
        number_column = 1
        while level_structure[number_line][number_column] == 'w' \
                or level_structure[number_line][number_column] == 'd'\
                or level_structure[number_line][number_column] == 'a'\
                or level_structure[number_line][number_column] == 'g':
            number_line = random.randint(0, 14)
            number_column = random.randint(0, 14)
        object_location = [number_column * SPRITE_SIZE, number_line * SPRITE_SIZE]
        return object_location


class Characters:
    """Create main character"""
    def __init__(self, picture, item_location):
        self.picture = pygame.image.load(picture).convert_alpha()
        self.picture = pygame.transform.scale(self.picture, (SPRITE_SIZE, SPRITE_SIZE))
        self.rectangle = self.picture.get_rect()
        self.rectangle.topleft = item_location
        self.objects_number = 0
        window.blit(self.picture, self.rectangle)

    def movement_right(self, character, level_structure):
        """the character moves to the right"""
        if character.rectangle[0] != window_width - SPRITE_SIZE:
            macgyver_location_maze[0] = int((character.rectangle[0] + SPRITE_SIZE) / SPRITE_SIZE)
            macgyver_location_maze[1] = int((character.rectangle[1]) / SPRITE_SIZE)
            if level_structure[macgyver_location_maze[1]][macgyver_location_maze[0]] != 'w':
                character.rectangle = character.rectangle.move(SPRITE_SIZE, 0)

    def movement_left(self, character, level_structure):
        """the character moves to the left"""
        if character.rectangle[0] != 0:
            macgyver_location_maze[0] = int((character.rectangle[0] - SPRITE_SIZE) / SPRITE_SIZE)
            macgyver_location_maze[1] = int((character.rectangle[1]) / SPRITE_SIZE)
            if level_structure[macgyver_location_maze[1]][macgyver_location_maze[0]] != 'w':
                character.rectangle = character.rectangle.move(-SPRITE_SIZE, 0)

    def movement_up(self, character, level_structure):
        """the character moves up"""
        if character.rectangle[1] != 0:
            macgyver_location_maze[0] = int((character.rectangle[0]) / SPRITE_SIZE)
            macgyver_location_maze[1] = int((character.rectangle[1] - SPRITE_SIZE) / SPRITE_SIZE)
            if level_structure[macgyver_location_maze[1]][macgyver_location_maze[0]] != 'w':
                character.rectangle = character.rectangle.move(0, -SPRITE_SIZE)

    def movement_down(self, character, level_structure):
        """the character moves down"""
        if character.rectangle[1] != window_width - SPRITE_SIZE:
            macgyver_location_maze[0] = int((character.rectangle[0]) / SPRITE_SIZE)
            macgyver_location_maze[1] = int((character.rectangle[1] + SPRITE_SIZE) / SPRITE_SIZE)
            if level_structure[macgyver_location_maze[1]][macgyver_location_maze[0]] != 'w':
                character.rectangle = character.rectangle.move(0, SPRITE_SIZE)

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