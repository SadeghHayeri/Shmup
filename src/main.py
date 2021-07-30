import pygame
import sys
from src.config import *
from src.game_manager import GameManager
from src.events import *


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((0, 0, 0))
    pygame.mouse.set_visible(False)

    game_manager = GameManager()
    player = game_manager.get_player()

    dt = 0
    while True:
        dt += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            # TODO: Remove
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                player.on_fire = True
            if event.type == pygame.MOUSEBUTTONUP:
                player.on_fire = False

        pygame.display.flip()
        screen.fill((0, 0, 0))
        game_manager.update(dt)
        game_manager.draw(screen)
        clock.tick(FPS)
