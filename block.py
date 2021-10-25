from ursina import *

# Normal block class
class NormalBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            color = "#AFFF3C",
            scale = (3, 0.8, 3),
            collider = "box",
            position = position,
            texture = "white_cube"
        )

# Jump block class
class JumpBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            color = "#FF8B00",
            scale = (3, 0.8, 3),
            collider = "box",
            position = position,
            texture = "white_cube"
        )

# Speed block class
class SpeedBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            color = "#53FFF5",
            scale = (3, 0.5, 8),
            collider = "box",
            position = position,
            texture = "white_cube"
        )
