import pygame
from settings import *
from random import randint
from pygame.locals import *

pygame.font.init()


# Food Object
class Food:
    def __init__(self, screen, x, y, color, size):
        self._screen = screen
        self._color = color
        self._size = size
        #self._img = pygame.image.load("res/apple.png")
        self.x = x
        self.y = y
        #self.img = pygame.transform.scale(self._img, (self._size, self._size))

    def regen(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(self._screen, self._color,
                         pygame.Rect(self.x * self._size, self.y * self._size, self._size, self._size)
                         )

    def clear(self, back_color):
        pygame.draw.rect(self._screen, back_color,
                         pygame.Rect(self.x * self._size, self.y * self._size, self._size, self._size)
                         )

    def check(self, x, y):
        # Check food position
        return self.x == x and self.y == y


# Snake Object
class Snake:
    def __init__(self, screen, x, y, color, size_block, vector):
        self._screen = screen
        self._vector = vector
        self._size_block = size_block
        self._color = color
        # add head
        self.body = [{"x": x, "y": y}]

    @property
    def head(self):
        return self.body[0]

    @property
    def vector(self):
        return self._vector

    @vector.setter
    def vector(self, vector):
        self._vector = vector

    def _move_block(self, block, x, y):
        prev_x, prev_y = block["x"], block["y"]
        block["x"] = x
        block["y"] = y
        return prev_x, prev_y

    def move(self, vector=None):
        if vector:
            self._vector = vector
        # Move a head
        delta_x, delta_y = direction_mapping[self._vector]
        prev_x, prev_y = self.body[0]["x"], self.body[0]["y"]
        self.body[0]["x"] += delta_x
        self.body[0]["y"] += delta_y
        # Move a body
        for i in range(1, len(self.body)):
            prev_x, prev_y = self._move_block(self.body[i], prev_x, prev_y)
        return prev_x, prev_y

    def grow(self, x, y):
        last_block = self.body[-1].copy()
        last_block["x"] = x
        last_block["y"] = y
        self.body.append(last_block)

    def draw(self):
        for block in self.body:
            pygame.draw.rect(self._screen, self._color, pygame.Rect(block["x"] * self._size_block,
                                                                    block["y"] * self._size_block,
                                                                    self._size_block,
                                                                    self._size_block))

    def clear(self, back_color):
        for block in self.body:
            pygame.draw.rect(self._screen, back_color, pygame.Rect(block["x"] * self._size_block,
                                                                   block["y"] * self._size_block,
                                                                   self._size_block,
                                                                   self._size_block))

    def check_pos(self, x, y):
        # Check coords in snake
        return False


class Game:
    def __init__(self, caption, icon_path):
        pygame.init()
        # Create the screen
        self._screen = pygame.display.set_mode((WIDTH * SIZE_IMG, HEIGHT * SIZE_IMG))
        # Title, Icon and Settings
        pygame.display.set_caption(caption)
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)
        self._score_font = pygame.font.SysFont("Britannic", 25, True)
        self._running = False
        self._food, self._snake = None, None
        self._score = 0

    def check(self):
        # Check head position
        return self._snake.head["x"] < 1 or self._snake.head["x"] >= WIDTH \
                or self._snake.head["y"] < 1 or self._snake.head["y"] >= HEIGHT

    def print_score(self):
        text = self._score_font.render("Score: " + str(self._score), True, ORANGE)
        self._screen.blit(text, [0, 0])

    def start_game(self):
        self._score = 0
        self._food = Food(self._screen, randint(0, WIDTH - 1), randint(0, HEIGHT - 1), RED, SIZE_IMG)
        # TODO: check food.x, food.y
        self._snake = Snake(self._screen,
                            randint(0, WIDTH - 1),
                            randint(0, HEIGHT - 1),
                            GREEN,
                            SIZE_IMG,
                            VECTORS[randint(0, 3)])
        self._running = True
        while self._running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            self._running = False
                        case pygame.K_LEFT:
                            self._snake.vector = "left"
                        case pygame.K_RIGHT:
                            self._snake.vector = "right"
                        case pygame.K_UP:
                            self._snake.vector = "up"
                        case pygame.K_DOWN:
                            self._snake.vector = "down"
                if event.type == QUIT:
                    self._running = False

            if self._score >= 20:
                self._running = False
            last_x, last_y = self._snake.move()
            self._screen.fill(BLACK)
            self.print_score()
            text = self._score_font.render("Coord: " + str(self._snake.head), True, ORANGE)
            self._screen.blit(text, [0, 30])
            self._food.draw()
            self._snake.draw()
            pygame.display.update()
            if self.check():
                self._running = False
            if self._food.check(*self._snake.head):
                self._snake.grow(last_x, last_y)
                self._food.regen(randint(0, WIDTH - 1), randint(0, HEIGHT - 1))
            pygame.time.wait(500)

    def stop_game(self):
        pygame.quit()


if __name__ == "__main__":
    game = Game("The Snake Game 1.0", ICON_PATH)
    game.start_game()
    game.stop_game()
