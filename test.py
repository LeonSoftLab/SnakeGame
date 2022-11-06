from random import randint
from settings import *

body_blocks = []
body_blocks.append([randint(0, WIDTH - 1), randint(0, HEIGHT - 1), VECTORS[randint(0, 3)]])
body_blocks.append([randint(0, WIDTH - 1), randint(0, HEIGHT - 1), VECTORS[randint(0, 3)]])
print(body_blocks)

print(type(body_blocks[0][0]))
body_blocks[0][0] += 2
body_blocks[0][1] += 5

print(range(0, len(body_blocks)))
print(len(body_blocks))

for i in range(1, len(body_blocks)):
    print(i)
    print(body_blocks[i])