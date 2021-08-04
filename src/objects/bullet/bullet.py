from src.objects.object import GameObject


class Bullet(GameObject):
    def __init__(self):
        super().__init__()

        self.speed = 1
        self.start_speed = 3
        self.max_speed = 7
        self.fire_time = 0
        self.damage = 30

    def update(self, dt):
        if not self.fire_time:
            self.fire_time = dt

        if self.speed < self.max_speed:
            self.speed = min((dt - self.fire_time) / 50 + self.start_speed, self.max_speed)

    def explode(self, dt):
        self.kill()
