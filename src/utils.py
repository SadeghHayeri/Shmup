import pygame
from numpy import uint8, minimum, array, float32, int32


def get_shadow(image, ambience=.1, color=(0, 0, 0)):
    img = image.copy().convert_alpha()
    img.fill(color, None, pygame.BLEND_RGBA_MULT)
    img.set_alpha(int(ambience * 255))
    return img
