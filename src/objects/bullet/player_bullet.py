from src.objects.bullet.bullet import Bullet
import pygame


class PlayerBullet(Bullet):
    def __init__(self, pos):
        super().__init__()
        self.level = 0
        self.width, self.height = 25, 25

        self.images = [
            pygame.transform.scale(pygame.image.load('src/assets/Tiles/tile_0000.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('src/assets/Tiles/tile_0001.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('src/assets/Tiles/tile_0002.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('src/assets/Tiles/tile_0003.png'), (self.width, self.height)),
        ]
        self.image = self.images[self.level]
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, dt):
        super().update(dt)
        self.rect.center = (self.rect.center[0], self.rect.center[1] - self.speed)
