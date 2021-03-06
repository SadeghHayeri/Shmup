from src.objects.bullet.bullet import Bullet
import pygame


class PlayerBullet(Bullet):
    def __init__(self, pos):
        super().__init__()
        self.level = 0
        self.damage = 30
        self.width, self.height = 30, 30

        self.images = [
            pygame.transform.scale(pygame.image.load('src/assets/Tiles/tile_0000.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('src/assets/Tiles/tile_0001.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('src/assets/Tiles/tile_0002.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('src/assets/Tiles/tile_0003.png'), (self.width, self.height)),
        ]
        self.image = self.images[self.level]
        self.rect = self.image.get_rect()
        self.pos = pos

    def update(self, dt):
        super().update(dt)
        self.pos = (self.pos[0], self.pos[1] - self.speed)
