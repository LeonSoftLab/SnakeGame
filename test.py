from random import randint
from settings import *
'''
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
'''


def _move_block(block, x, y):
    prev_x, prev_y = block["x"], block["y"]
    block["x"] = x
    block["y"] = y
    return prev_x, prev_y

body = [{"x": 10, "y": 15}, {"x": 11, "y": 15}, {"x": 12, "y": 15}, {"x": 12, "y": 16}]
delta_x, delta_y = direction_mapping["left"]
prev_x, prev_y = body[0]["x"], body[0]["y"]
body[0]["x"] += delta_x
body[0]["y"] += delta_y
# Move a body
for i in range(1, len(body)):
    prev_x, prev_y = _move_block(body[i], prev_x, prev_y)
