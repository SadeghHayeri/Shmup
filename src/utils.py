import pygame
from numpy import uint8, minimum, array, float32, int32


def get_shadow(image, ambience=.1):
    if ambience is None:
        ambience = 0.0
    elif not (0.0 <= ambience <= 1.0):
        raise ValueError("ambience must be between 0.0 and 1.0 inclusive")
    if image.get_masks()[3] != 0:
        image_alpha = pygame.surfarray.pixels_alpha(image)
        if ambience > 0.0:
            shadow_alpha = (image_alpha *
                            (1.0 - ambience)).astype(uint8)
        else:
            shadow_alpha = image_alpha
    elif image.get_colorkey() is not None:
        image_alpha = pygame.surfarray.array_colorkey(image)
        image.unlock()
        image.unlock()  # pygame 1.7 bug (fixed in 1.8).
        surface_alpha = image.get_alpha()
        if surface_alpha is not None:
            # Do what array_colorkey should have done: use surface alpha!
            minimum(image_alpha, surface_alpha, image_alpha)
        if ambience > 0.0:
            shadow_alpha = (image_alpha *
                            (1.0 - ambience)).astype(uint8)
        else:
            shadow_alpha = image_alpha
    else:
        image_alpha = image.get_alpha()
        if image_alpha is None:
            image_alpha = 255
        shadow_alpha = int(image_alpha * (1.0 - ambience))
    shadow = image.convert_alpha()
    shading = pygame.Surface(shadow.get_size(), pygame.SRCALPHA, 32)
    pygame.surfarray.pixels_alpha(shading)[...] = image_alpha
    shadow.blit(shading, (0, 0))
    pygame.surfarray.pixels_alpha(shadow)[...] = shadow_alpha
    return shadow
