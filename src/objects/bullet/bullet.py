from src.objects.object import GameObject
import pygame
import random

EXPLODE_IMAGES = [
    pygame.image.load('src/assets/Tiles/tile_0004.png'),
    pygame.image.load('src/assets/Tiles/tile_0005.png'),
]


class Bullet(GameObject):
    def __init__(self):
        super().__init__()

        self.speed = 1
        self.start_speed = 3
        self.max_speed = 7
        self.fire_time = 0
        self.damage = 30
        self.exploded = False
        self.explode_time = None

    def update(self, dt):
        super(Bullet, self).update(dt)
        if self.exploded:
            if self.explode_time <= dt - 5:
                self.kill()
        else:
            if not self.fire_time:
                self.fire_time = dt

            if self.speed < self.max_speed:
                self.speed = min((dt - self.fire_time) / 50 + self.start_speed, self.max_speed)

    def explode(self, dt):
        # self.speed = 0
        # self.max_speed = 0
        self.exploded = True
        self.explode_time = dt
        self.pos = (self.pos[0], self.pos[1] - 50)

        size = random.randint(20, 40)
        self.image = random.choice(EXPLODE_IMAGES)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.image = pygame.transform.rotate(self.image, random.randint(0, 180))
