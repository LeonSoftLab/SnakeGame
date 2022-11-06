import pygame
import copy
from settings import *
from random import randint
from pygame.locals import *

pygame.font.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH * SIZE_IMG, HEIGHT * SIZE_IMG))

# Title, Icon and Settings
pygame.display.set_caption("The snake game")
icon = pygame.image.load("res/snake.png")
pygame.display.set_icon(icon)
score_font = pygame.font.SysFont("Britannic", 25, True)


def move_block(block, vector, step: int):
    if vector == "left" and block[0] >= step:
        block[0] -= step
    if vector == "right" and block[0] <= WIDTH - step:
        block[0] += step
    if vector == "up" and block[1] >= step:
        block[1] -= step
    if vector == "down" and block[1] <= HEIGHT - step:
        block[1] += step
    block[2] = vector


# Food Object
class Food:
    def __init__(self, screen):
        self._screen = screen
        #self._img = pygame.image.load("res/apple.png")
        self.x = randint(0, WIDTH - 1)
        self.y = randint(0, HEIGHT - 1)
        #self.img = pygame.transform.scale(self._img, (SIZE_IMG, SIZE_IMG))

    def regen(self):
        self.x = randint(0, WIDTH - 1)
        self.y = randint(0, HEIGHT - 1)

    def draw(self):
        #self._screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(self._screen, RED, pygame.Rect(self.x * SIZE_IMG, self.y * SIZE_IMG, SIZE_IMG, SIZE_IMG))
        #pygame.display.flip()


# Snake Object
class Snake:
    def __init__(self, screen):
        self._screen = screen
        self.body = []
        # add head
        self.body.append([randint(0, WIDTH - 1),
                          randint(0, HEIGHT - 1),
                          VECTORS[randint(0, 3)]])

    @property
    def head(self):
        return self.body[0]

    def move(self, vector):
        # Move a head
        move_block(self.body[0], vector, 1)
        # Move a body
        for i in range(1, len(self.body)):
            move_block(self.body[i], self.body[i-1][2], 1)

    def grow(self):
        self.body.append(self.body[-1].copy())
        move_block(self.body[-1], self.body[-1][2], -1)

    def draw(self):
        for block in self.body:
            pygame.draw.rect(self._screen, GREEN, pygame.Rect(block[0] * SIZE_IMG,
                                                              block[1] * SIZE_IMG,
                                                              SIZE_IMG,
                                                              SIZE_IMG))


def print_score(score):
    text = score_font.render("Score: " + str(score), True, ORANGE)
    screen.blit(text, [0, 0])


def start_game():

    score = 0
    food1 = Food(screen)
    snake1 = Snake(screen)

    def check_objects():
        if False:
            score += 1

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        running = False
                    case pygame.K_LEFT:
                        snake1.head[2] = "left"
                    case pygame.K_RIGHT:
                        snake1.head[2] = "right"
                    case pygame.K_UP:
                        snake1.head[2] = "up"
                    case pygame.K_DOWN:
                        snake1.head[2] = "down"
            if event.type == QUIT:
                running = False

        if score >= 20:
            running = False
        snake1.move(snake1.head[2])
        check_objects()
        screen.fill(BLACK)
        print_score(score)
        food1.draw()
        snake1.draw()
        pygame.display.update()
        pygame.time.wait(1000 // (score + 1))
    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    start_game()
    pygame.quit()
