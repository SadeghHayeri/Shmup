from src.objects.object import GameObject
import pygame
from src.utils import get_shadow


class Ship(GameObject):
    def __init__(self):
        super().__init__()

        self.health = 1000
        self.has_shadow = True
        self.last_hit_time = None
        self.original_image = None
        self.hit_image = None

    def hit(self, dt, damage):
        self.last_hit_time = dt
        self.health -= damage
        if self.health <= 0:
            self.kill()

    def _get_hit_image(self):
        shadow = get_shadow(self.image, .5, (255, 0, 0))
        result = pygame.Surface(self.image.get_size(), pygame.SRCALPHA, 32)
        result.blit(self.image, (0, 0))
        result.blit(shadow, (0, 0))
        return result

    def update(self, dt):
        if dt == 1:
            self.original_image = self.image.copy()
            self.hit_image = self._get_hit_image()

        if self.last_hit_time and dt - 6 <= self.last_hit_time <= dt:
            self.image = self.hit_image
        else:
            self.image = self.original_image

