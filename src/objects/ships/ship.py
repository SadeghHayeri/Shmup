from src.objects.object import GameObject
import pygame
from src.utils import get_shadow
import random

EXPLODE_SOUND_FXS = [
    pygame.mixer.Sound('src/assets/sounds/explode/00.wav'),
    pygame.mixer.Sound('src/assets/sounds/explode/01.wav'),
    pygame.mixer.Sound('src/assets/sounds/explode/02.wav'),
    pygame.mixer.Sound('src/assets/sounds/explode/03.wav'),
]


class Ship(GameObject):
    def __init__(self):
        super().__init__()

        self.health = 100
        self.has_shadow = True
        self.last_hit_time = None
        self.original_image = None
        self.hit_image = None
        self.exploded = False
        self.explode_time = None
        self.explode_size = random.uniform(.7, 1.3)
        self.explode_duration = random.randint(4, 7)

    def hit(self, dt, damage):
        self.last_hit_time = dt
        self.health -= damage
        if not self.exploded and self.health <= 0:
            self.exploded = True
            sound = random.choice(EXPLODE_SOUND_FXS)
            sound.set_volume(.8)
            sound.play()

    def _get_hit_image(self):
        shadow = get_shadow(self.image, .5, (255, 0, 0))
        result = pygame.Surface(self.image.get_size(), pygame.SRCALPHA, 32)
        result.blit(self.image, (0, 0))
        result.blit(shadow, (0, 0))
        return result

    def _get_explode_images(self, image_index):
        result = pygame.Surface(self.image.get_size(), pygame.SRCALPHA, 32)

        explode_size = (
            int(self.explode_size * self.image.get_size()[0]),
            int(self.explode_size * self.image.get_size()[0])
        )
        img = [
            pygame.transform.scale(pygame.image.load('src/assets/Tiles/tile_0005.png'), explode_size),
            pygame.transform.scale(pygame.image.load('src/assets/Tiles/tile_0007.png'), explode_size),
            pygame.transform.scale(pygame.image.load('src/assets/Tiles/tile_0008.png'), explode_size),
        ][image_index]

        # result.blit(self.original_image, (0, 0))
        result.blit(img, (self.image.get_size()[0] // 2 - explode_size[0] // 2, self.image.get_size()[1] // 2 - explode_size[1] // 2))
        return result

    def init(self, dt):
        super(Ship, self).init(dt)

        self.original_image = self.image.copy()
        self.hit_image = self._get_hit_image()

    def update(self, dt):
        super(Ship, self).update(dt)

        if self.exploded:
            if self.explode_time is None:
                self.explode_time = dt
                self.image = self._get_explode_images(0)
            elif self.explode_time == dt - self.explode_duration:
                self.image = self._get_explode_images(1)
            elif self.explode_time == dt - 2 * self.explode_duration:
                self.image = self._get_explode_images(2)
            elif self.explode_time == dt - 3 * self.explode_duration:
                self.kill()
        else:
            if self.last_hit_time and dt - 6 <= self.last_hit_time <= dt:
                self.image = self.hit_image
            else:
                self.image = self.original_image

