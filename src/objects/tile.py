from src.objects.object import GameObject
import pygame
from src.config import *


TILE_WIDTH, TILE_HEIGHT = 40, 40


def get_image(path):
    return pygame.transform.scale(pygame.image.load(path), (TILE_WIDTH, TILE_HEIGHT))

# left, top, right, bottom
# down-left, top-left, top-right, down-right
TILE_IMAGES = {
    'b:b:b:b,b:b:b:b': get_image('src/assets/Tiles/tile_0042.png'),

    'b:b:b:b,b:b:b:g': get_image('src/assets/Tiles/tile_0037.png'),
    'b:b:b:b,b:b:g:b': get_image('src/assets/Tiles/tile_0061.png'),
    'b:b:b:b,b:g:b:b': get_image('src/assets/Tiles/tile_0063.png'),
    'b:b:b:b,g:b:b:b': get_image('src/assets/Tiles/tile_0039.png'),

    'b:b:b:g,g:b:b:g': get_image('src/assets/Tiles/tile_0038.png'),
    'b:b:b:g,g:b:b:b': get_image('src/assets/Tiles/tile_0038.png'),
    'b:b:b:g,b:b:b:g': get_image('src/assets/Tiles/tile_0038.png'),
    'b:b:b:g,b:b:b:b': get_image('src/assets/Tiles/tile_0038.png'),

    'b:b:g:b,b:b:g:g': get_image('src/assets/Tiles/tile_0049.png'),
    'b:b:g:b,b:b:b:g': get_image('src/assets/Tiles/tile_0049.png'),
    'b:b:g:b,b:b:g:b': get_image('src/assets/Tiles/tile_0049.png'),
    'b:b:g:b,b:b:b:b': get_image('src/assets/Tiles/tile_0049.png'),

    'b:g:b:b,b:b:b:b': get_image('src/assets/Tiles/tile_0062.png'),
    'b:g:b:b,b:g:g:b': get_image('src/assets/Tiles/tile_0062.png'),
    'b:g:b:b,b:b:g:b': get_image('src/assets/Tiles/tile_0062.png'),
    'b:g:b:b,b:g:b:b': get_image('src/assets/Tiles/tile_0062.png'),

    'g:b:b:b,b:b:b:b': get_image('src/assets/Tiles/tile_0051.png'),
    'g:b:b:b,g:g:b:b': get_image('src/assets/Tiles/tile_0051.png'),
    'g:b:b:b,g:b:b:b': get_image('src/assets/Tiles/tile_0051.png'),
    'g:b:b:b,b:g:b:b': get_image('src/assets/Tiles/tile_0051.png'),

    'b:g:g:b,b:b:g:b': get_image('src/assets/Tiles/tile_0041.png'),
    'b:g:g:b,b:g:g:b': get_image('src/assets/Tiles/tile_0041.png'),
    'b:b:g:g,b:b:b:g': get_image('src/assets/Tiles/tile_0053.png'),
    'b:b:g:g,b:b:g:g': get_image('src/assets/Tiles/tile_0053.png'),
    'g:b:b:g,g:b:b:b': get_image('src/assets/Tiles/tile_0052.png'),
    'g:g:b:b,b:g:b:b': get_image('src/assets/Tiles/tile_0040.png'),
    'g:g:b:b,b:g:g:b': get_image('src/assets/Tiles/tile_0040.png'),

    # Brown

    'b:b:b:b,b:b:b:x': get_image('src/assets/Tiles/tile_0043.png'),
    'b:b:b:b,b:b:x:b': get_image('src/assets/Tiles/tile_0067.png'),
    'b:b:b:b,b:x:b:b': get_image('src/assets/Tiles/tile_0069.png'),
    'b:b:b:b,x:b:b:b': get_image('src/assets/Tiles/tile_0045.png'),

    'b:b:b:x,x:b:b:x': get_image('src/assets/Tiles/tile_0044.png'),
    'b:b:b:x,x:b:b:b': get_image('src/assets/Tiles/tile_0044.png'),
    'b:b:b:x,b:b:b:x': get_image('src/assets/Tiles/tile_0044.png'),
    'b:b:b:x,b:b:b:b': get_image('src/assets/Tiles/tile_0044.png'),

    'b:b:x:b,b:b:x:x': get_image('src/assets/Tiles/tile_0055.png'),
    'b:b:x:b,b:b:b:x': get_image('src/assets/Tiles/tile_0055.png'),
    'b:b:x:b,b:b:x:b': get_image('src/assets/Tiles/tile_0055.png'),
    'b:b:x:b,b:b:b:b': get_image('src/assets/Tiles/tile_0055.png'),

    'b:x:b:b,b:b:b:b': get_image('src/assets/Tiles/tile_0068.png'),
    'b:x:b:b,b:x:x:b': get_image('src/assets/Tiles/tile_0068.png'),
    'b:x:b:b,b:b:x:b': get_image('src/assets/Tiles/tile_0068.png'),
    'b:x:b:b,b:x:b:b': get_image('src/assets/Tiles/tile_0068.png'),

    'x:b:b:b,b:b:b:b': get_image('src/assets/Tiles/tile_0057.png'),
    'x:b:b:b,x:x:b:b': get_image('src/assets/Tiles/tile_0057.png'),
    'x:b:b:b,x:b:b:b': get_image('src/assets/Tiles/tile_0057.png'),
    'x:b:b:b,b:x:b:b': get_image('src/assets/Tiles/tile_0057.png'),

    'b:x:x:b,b:b:x:b': get_image('src/assets/Tiles/tile_0047.png'),
    'b:b:x:x,b:b:b:x': get_image('src/assets/Tiles/tile_0059.png'),
    'x:b:b:x,x:b:b:b': get_image('src/assets/Tiles/tile_0058.png'),
    'x:b:b:x,x:b:b:x': get_image('src/assets/Tiles/tile_0058.png'),
    'x:x:b:b,b:x:b:b': get_image('src/assets/Tiles/tile_0046.png'),
    'x:x:b:b,b:x:x:b': get_image('src/assets/Tiles/tile_0046.png'),

    'green': get_image('src/assets/Tiles/tile_0050.png'),
    'brown': get_image('src/assets/Tiles/tile_0056.png'),
}


INDEX_MAPPING = {
    'B': 'b',
    'G': 'g',
    'X': 'x'
}


class Tile(GameObject):
    def __init__(self, game_map, x, y):
        super().__init__()

        self.x, self.y = x, y
        map_width, map_height = len(game_map), len(game_map[0])

        if x == 0 or x == map_width - 1 or y == 0 or y == map_height - 1:
            self.image = TILE_IMAGES['b:b:b:b,b:b:b:b']
        elif INDEX_MAPPING[game_map[x][y]] == 'g':
            self.image = TILE_IMAGES['green']
        elif INDEX_MAPPING[game_map[x][y]] == 'x':
            self.image = TILE_IMAGES['brown']
        else:
            left_index = INDEX_MAPPING[game_map[x - 1][y]]
            top_index = INDEX_MAPPING[game_map[x][y - 1]]
            right_index = INDEX_MAPPING[game_map[x + 1][y]]
            bottom_index = INDEX_MAPPING[game_map[x][y + 1]]

            bottom_left_index = INDEX_MAPPING[game_map[x - 1][y + 1]]
            top_left_index = INDEX_MAPPING[game_map[x - 1][y - 1]]
            top_right_index = INDEX_MAPPING[game_map[x + 1][y - 1]]
            bottom_right_index = INDEX_MAPPING[game_map[x + 1][y + 1]]

            tile_index = f"{left_index}:{top_index}:{right_index}:{bottom_index},{bottom_left_index}:{top_left_index}:{top_right_index}:{bottom_right_index}"
            self.image = TILE_IMAGES[tile_index]

        self.rect = self.image.get_rect()
        self.rect.center = (x * TILE_WIDTH, y * TILE_HEIGHT)
        self.initial_diff_pos = -1 * map_height * TILE_HEIGHT + HEIGHT
        self.speed = 1

    def update(self, dt):
        diff_pos = self.initial_diff_pos + self.speed * dt
        self.rect.center = (self.x * TILE_WIDTH, self.y * TILE_HEIGHT + diff_pos)

