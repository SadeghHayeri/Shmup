from src.objects.ships.player_ship import PlayerShip
from src.objects.bullet.player_bullet import PlayerBullet
from pygame import sprite
from src.config import FPS


class GameManager:
    def __init__(self):
        self.players = sprite.Group()
        self.bullets = sprite.Group()

        self.player = PlayerShip()
        self.players.add(self.player)

    def get_player(self):
        return self.player

    def update(self, dt):
        self.players.update(dt)
        self.bullets.update(dt)

        if self.player.on_fire:
            if dt % (FPS / (1000 // (1 / self.player.fire_rate))) == 0:
                self.fire(dt)

    def fire(self, dt):
        self.player.fire(dt)
        bullet = PlayerBullet(self.player.rect.center)
        self.bullets.add(bullet)

    def draw(self, screen):
        self.bullets.draw(screen)
        self.players.draw(screen)


