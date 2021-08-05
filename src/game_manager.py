from src.objects.ships.player_ship import PlayerShip
from src.objects.ships.enemy_ship import EnemyShip
from src.objects.bullet.player_bullet import PlayerBullet
from src.objects.tile import Tile
from src.config import *
from pygame import sprite
from src.config import FPS
import pygame
import random


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
        self.enemies = sprite.Group()
        self.bullets = sprite.Group()
        self.shadows = sprite.Group()
        self.map = sprite.Group()

        self.player = PlayerShip()
        self.players.add(self.player)
        self.shadows.add(self.player.get_shadow())

        # TODO: Render only onscreen tiles
        for tile in get_map():
            self.map.add(tile)

        background_sound = pygame.mixer.Sound('src/assets/sounds/background/00.wav')
        background_sound.set_volume(.2)
        background_sound.play(loops=True, fade_ms=2000)

    def get_player(self):
        return self.player

    def _check_bullet_collision(self, dt):
        for bullet in filter(lambda b: not b.exploded, self.bullets):
            collides = pygame.sprite.spritecollide(bullet, self.enemies, False)
            if collides:
                bullet.explode(dt)
                for collide in collides:
                    collide.hit(dt, bullet.damage)

    def update(self, dt):
        self.map.update(dt)
        self.players.update(dt)
        self.enemies.update(dt)
        self.bullets.update(dt)
        self.shadows.update(dt)

        if random.random() > .99:
            ship_type = random.choice(['b1', 'b2', 'b3', 'b4', 's1', 's2', 's3', 's4'])
            start_pos = (random.randint(100, WIDTH - 100), -100)
            enemy = EnemyShip(ship_type, start_pos, random.choice([-45, 0, 45]))
            self.enemies.add(enemy)
            self.shadows.add(enemy.get_shadow())

        if self.player.on_fire:
            if dt % (FPS / (1000 // (1 / self.player.fire_rate))) == 0:
                self.fire(dt)

        self._check_bullet_collision(dt)

    def fire(self, dt):
        self.player.fire(dt)
        bullet = PlayerBullet(self.player.rect.center)
        self.bullets.add(bullet)

    def draw(self, screen):
        self.map.draw(screen)
        self.shadows.draw(screen)
        self.enemies.draw(screen)
        self.bullets.draw(screen)
        self.players.draw(screen)


