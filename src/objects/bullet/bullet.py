from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self):
        super().__init__()

        self.speed = 1
