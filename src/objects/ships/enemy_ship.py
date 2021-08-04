from src.objects.ships.ship import Ship
import pygame


def get_image(path, size):
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, 180)
    return image


SHIP_IMAGES = {
    'b1': get_image('src/assets/Ships/ship_0000.png', (100, 100)),
    'b2': get_image('src/assets/Ships/ship_0001.png', (100, 100)),
    'b3': get_image('src/assets/Ships/ship_0002.png', (100, 100)),
    'b4': get_image('src/assets/Ships/ship_0003.png', (100, 100)),
    's1': get_image('src/assets/Ships/ship_0004.png', (80, 80)),
    's2': get_image('src/assets/Ships/ship_0005.png', (80, 80)),
    's3': get_image('src/assets/Ships/ship_0006.png', (80, 80)),
    's4': get_image('src/assets/Ships/ship_0007.png', (80, 80)),
}


class EnemyShip(Ship):
    def __init__(self, _type, start_pos, end_pos):
        super().__init__()
        self.image = SHIP_IMAGES[_type]
        self.rect = self.image.get_rect()
        self.pos = start_pos

        self.on_fire = False
        self.fire_rate = 1 / 300
        self.fire_time = 0
        self.speed = 2

    def _update_ship_location(self, dt):
        self.pos = (self.pos[0], self.pos[1] + self.speed)

    def update(self, dt):
        super(EnemyShip, self).update(dt)
        self._update_ship_location(dt)

    def fire(self, fire_time):
        self.fire_time = fire_time
