from src.objects.object import GameObject


class Ship(GameObject):
    def __init__(self):
        super().__init__()

        self.has_shadow = True

