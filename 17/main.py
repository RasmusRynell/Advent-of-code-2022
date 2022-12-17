import json
import sys
import os
#import torch
import numpy as np
import matplotlib.pyplot as plt
import time

plt.ion()

''' input:
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
'''

rocks = ['-', '+', 'J', 'l', 'o']

def get_index_of_rock(rock_char):
    return rocks.index(rock_char) + 1

def get_starting_y(stack):
    # In all of stack in what row is the last non-zero element
    for y in range(2022*4-1, -1, -1):
        for x in range(7):
            if stack[y][x] != 0:
                return y + 4
    return 3

def overlap_with_stack(stack, rock):
    for x,y in rock:
        if stack[y][x] != 0:
            return True
    return False

def make_rock(rock_char, x, y):
    if rock_char == '-':
        return [[x,y], [x+1,y], [x+2,y], [x+3,y]]
    elif rock_char == '+':
        return [[x+1,y], [x,y+1], [x+1,y+1], [x+2,y+1], [x+1,y+2]]
    elif rock_char == 'J':
        return [[x,y], [x+1,y], [x+2,y], [x+2,y+1], [x+2,y+2]]
    elif rock_char == 'l':
        return [[x,y], [x,y+1], [x,y+2], [x,y+3 ]]
    elif rock_char == 'o':
        return [[x,y], [x+1,y], [x,y+1], [x+1,y+1]]

def push_rock(rock, stream):
    old_rock = rock
    if stream == '>':
        rock = [[x+1,y] for x,y in rock]
    elif stream == '<':
        rock = [[x-1,y] for x,y in rock]

    # check if rock is out of bounds
    if any([x < 0 or x > 6 for x,y in rock]):
        return old_rock

    # check if rock is overlapping with stack
    if overlap_with_stack(stack, rock):
        return old_rock

    return rock

def move_down(rock):
    old_rock = rock
    rock = [[x,y-1] for x,y in rock]

    # check if rock is out of bounds
    if any([y < 0 for x,y in rock]):
        return old_rock

    # check if rock is overlapping with stack
    if overlap_with_stack(stack, rock):
        return old_rock

    return rock

def draw(stack, rock, delay=0.1):
    # Plot stack
    plt.clf()
    plt.imshow(stack[0:25,:])

    # Plot rock
    for x,y in current_rock:
        plt.scatter(x, y, color='red')

    plt.pause(delay)
    plt.draw()

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        jet_stream = f.read()

    stack = np.zeros((2022*4, 7))
    total_rocks = 2022

    #print(jet_stream, flush=True)

    j = 0
    for i in range(0, 2022):
        x = 2
        y = get_starting_y(stack)
        #print(x, y, flush=True)
        current_rock_char = rocks[i%len(rocks)]
        current_rock = make_rock(current_rock_char, x, y)
        #draw(stack, current_rock)

        while True:
            current_stream = jet_stream[j%len(jet_stream)]
            j += 1

            # Move rock side to side
            #print(f"Rock pushed {current_stream}", flush=True)
            current_rock = push_rock(current_rock, current_stream)

            #draw(stack, current_rock)

            # Move rock down
            old_curr = current_rock
            current_rock = move_down(current_rock)

            #draw(stack, current_rock)

            if current_rock == old_curr:
                # Rock is at the bottom
                # Add rock to stack
                for x,y in current_rock:
                    stack[y][x] = get_index_of_rock(current_rock_char)
                break

    # Current height of stack
    height = get_starting_y(stack)
    print(f"Stack height: {height-3}", flush=True)

    #plt.ioff()
    #plt.imshow(stack[0:height,:])
    #plt.show()