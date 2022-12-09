import json
import sys
import pandas as pd
import numpy as np

time = 0
p1 = False
should_draw = False

if p1:
    grid_size_x = len("......")
    grid_size_y = len(".....")
    offset_x=0
    offset_y=0

else:
    grid_size_x = len("..........................")
    grid_size_y = len(".....................")
    offset_x=12
    offset_y=6

def draw(time, rope, grid_size_x, grid_size_y):
    global offset_x, offset_y, should_draw
    if should_draw:
        print(f'-------{time}--------')
        for y in range(grid_size_y, 0, -1):
            y = y - offset_y
            for x in range(1, grid_size_x, 1):
                x = x - offset_x
                if (x, y) in rope:
                    pos_in_rope = rope.index((x, y))
                    if pos_in_rope == 0:
                        print('H', end='')
                    elif pos_in_rope == len(rope)-1:
                        print('T', end='')
                    else:
                        print(pos_in_rope, end='')
                else:
                    print('.', end='')
            print('')
        print('-----------------')


def update_tail(rope):
    for i in range(1, len(rope)):
        T_x = rope[i][0]
        T_y = rope[i][1]
        H_x = rope[i-1][0]
        H_y = rope[i-1][1]

        delta_x = H_x - T_x
        delta_y = H_y - T_y

        if delta_x > 1:
            if delta_y > 0:
                T_y += 1
            elif delta_y < 0:
                T_y -= 1
            T_x += 1

        elif delta_x < -1:
            if delta_y > 0:
                T_y += 1
            elif delta_y < 0:
                T_y -= 1
            T_x -= 1

        elif delta_y > 1:
            T_y += 1
            if delta_x > 0:
                T_x += 1
            elif delta_x < 0:
                T_x -= 1

        elif delta_y < -1:
            T_y -= 1
            if delta_x > 0:
                T_x += 1
            elif delta_x < 0:
                T_x -= 1

        tails_new_pos = (T_x, T_y)
        rope[i] = tails_new_pos

        if i == len(rope)-1:
            if tails_new_pos not in tails_visited:
                tails_visited.append(tails_new_pos)




def update_head(rope, direction, num_of_steps):
    global time, grid_size_x, grid_size_y
    H_x = rope[0][0]
    H_y = rope[0][1]
    for i in range(int(num_of_steps)):
        if direction == 'R':
            H_x += 1
        elif direction == 'L':
            H_x -= 1
        elif direction == 'U':
            H_y += 1
        elif direction == 'D':
            H_y -= 1
        rope[0] = (H_x, H_y)
        update_tail(rope)
        draw(time, rope, grid_size_x, grid_size_y)
        time += 1



if __name__ == "__main__":
    if p1:
        rope = [(0,0)]*2
    else:
        rope = [(0,0)]*10

    tails_visited = [(0,0)]

    with open('input.txt', 'r') as f:
        draw(time, rope, grid_size_x, grid_size_y)
        for line in f:
            direction, num_of_steps = line.split()
            if should_draw:
                print(f'== {direction, num_of_steps} ==')
            update_head(rope, direction, num_of_steps)

    print(f'Tail visited {len(tails_visited)} different positions')