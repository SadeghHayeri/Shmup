import pygame
pygame.init()

import sys
from src.config import *
from src.game_manager import GameManager
from src.events import *


if __name__ == '__main__':
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
        screen.fill((100, 100, 100))
        game_manager.update(dt)
        game_manager.draw(screen)

        font = pygame.font.Font(None, 18)
        fps = font.render(f'{int(clock.get_fps())} FPS', True, pygame.Color('black') if clock.get_fps() > 55 else pygame.Color('red'))
        screen.blit(fps, (5, 5))
        clock.tick(FPS)
