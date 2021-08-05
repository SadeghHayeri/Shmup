from src.objects.object import GameObject
import pygame
import random

EXPLODE_IMAGES = [
    pygame.image.load('src/assets/Tiles/tile_0004.png'),
    pygame.image.load('src/assets/Tiles/tile_0005.png'),
]
EXPLODE_SOUND_FXS = [
    pygame.mixer.Sound('src/assets/sounds/hit/00.wav'),
    pygame.mixer.Sound('src/assets/sounds/hit/01.wav'),
    pygame.mixer.Sound('src/assets/sounds/hit/02.wav'),
    pygame.mixer.Sound('src/assets/sounds/hit/03.wav'),
]

MISSILE_SOUND_FXS = [
    pygame.mixer.Sound('src/assets/sounds/missile/00.wav'),
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

        sound = random.choice(MISSILE_SOUND_FXS)
        sound.set_volume(.1)
        sound.play()

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
        random.choice(EXPLODE_SOUND_FXS).play()
        # self.speed = 0
        # self.max_speed = 0
        self.exploded = True
        self.explode_time = dt
        self.pos = (self.pos[0], self.pos[1] - 50)

        size = random.randint(20, 40)
        self.image = random.choice(EXPLODE_IMAGES)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.image = pygame.transform.rotate(self.image, random.randint(0, 180))
