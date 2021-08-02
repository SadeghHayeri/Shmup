from src.objects.ships.player_ship import PlayerShip
from src.objects.bullet.player_bullet import PlayerBullet
from src.objects.tile import Tile
from pygame import sprite
from src.config import FPS


def get_map():
    with open('src/map.txt', 'r') as f:
        game_map = [list(line.strip().replace(' ', '')) for line in f.readlines()]
        game_map = list(zip(*list(reversed(game_map))[::-1]))

    result = []
    for x, row in enumerate(game_map):
        for y, item in enumerate(row):
            result.append(Tile(game_map, x, y))
    return result


class GameManager:
    def __init__(self):
        self.players = sprite.Group()
        self.bullets = sprite.Group()
        self.shadows = sprite.Group()
        self.map = sprite.Group()

        self.player = PlayerShip()
        self.players.add(self.player)
        self.shadows.add(self.player.get_shadow())

        for tile in get_map():
            self.map.add(tile)

    def get_player(self):
        return self.player

    def update(self, dt):
        self.players.update(dt)
        self.bullets.update(dt)
        self.shadows.update(dt)

        if self.player.on_fire:
            if dt % (FPS / (1000 // (1 / self.player.fire_rate))) == 0:
                self.fire(dt)

    def fire(self, dt):
        self.player.fire(dt)
        bullet = PlayerBullet(self.player.rect.center)
        self.bullets.add(bullet)

    def draw(self, screen):
        self.map.draw(screen)
        self.shadows.draw(screen)
        self.bullets.draw(screen)
        self.players.draw(screen)


