# Global settings
SIZE_IMG = 32
WIDTH, HEIGHT = 25, 20  # Map
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (40, 225, 70)
RED = (255, 0, 0)
FPS = 60
ICON_PATH = "res/snake.png"
VECTORS = ("left", "up", "right", "down")
direction_mapping = {
    "left": (-1, 0),
    "right": (1, 0),
    "up": (0, -1),
    "down": (0, 1)
}