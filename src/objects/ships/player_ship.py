from src.objects.ships.ship import Ship
import pygame


class PlayerShip(Ship):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('src/assets/Ships/ship_0000.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()

        self.on_fire = False
        self.fire_rate = 1 / 300
        self.fire_time = 0
        self.fire_pos_diff = 0

    def _update_fire_pos_diff(self, dt):
        diff = dt - self.fire_time
        if diff < 5:
            self.fire_pos_diff = self.fire_pos_diff + 1
        elif self.fire_pos_diff >= 0:
            self.fire_pos_diff = self.fire_pos_diff - 1

    def _update_ship_location(self, dt):
        self._update_fire_pos_diff(dt)
        mouse_pos = pygame.mouse.get_pos()
        self.rect.center = (mouse_pos[0], mouse_pos[1] + self.fire_pos_diff)

    def update(self, dt):
        self._update_ship_location(dt)

    def fire(self, fire_time):
        self.fire_time = fire_time
