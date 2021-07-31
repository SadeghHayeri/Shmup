from pygame.sprite import Sprite
from src.utils import get_shadow
import pygame


class Shadow(Sprite):
    def __init__(self, owner, offset, scale, ambience):
        super().__init__()
        self.owner = owner
        self.offset = offset
        self.scale = scale
        self.image = get_shadow(owner.image, ambience)
        self.image = pygame.transform.scale(self.image, (owner.rect.width, owner.rect.height))
        self.rect = self.image.get_rect()

    def update(self, dt):
        if not self.owner.alive():
            self.kill()

        owner_center = self.owner.rect.center
        self.rect.center = (owner_center[0] + self.offset[0], owner_center[1] + self.offset[1])


class GameObject(Sprite):
    def __init__(self):
        super().__init__()

        self.has_shadow = False
        self.shadow_offset = (-30, 20)
        self.shadow_scale = .9
        self.shadow_ambience = .9

    def get_shadow(self):
        if self.has_shadow:
            return Shadow(self, self.shadow_offset, self.shadow_scale, self.shadow_ambience)