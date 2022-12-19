import json
import sys
import os
#import torch
import numpy as np
import matplotlib.pyplot as plt
import time

def is_inside_testing_zone(pos, min_x, max_x, min_y, max_y, min_z, max_z):
    return min_x-1 <= pos[0] <= max_x+1 and min_y-1 <= pos[1] <= max_y+1 and min_z-1 <= pos[2] <= max_z+1

def get_neighbor(pos):
    neighbor = []
    for i in range(-1, 2, 2):
        neighbor.append((pos[0]+i, pos[1], pos[2]))
        neighbor.append((pos[0], pos[1]+i, pos[2]))
        neighbor.append((pos[0], pos[1], pos[2]+i))
    return neighbor

def get_outside(blocks, min_x, max_x, min_y, max_y, min_z, max_z):
    outside = []
    curr = (min_x, min_y, min_z)
    frontier = [curr]
    while len(frontier) > 0:
        curr = frontier.pop(0)
        if curr not in outside:
            outside.append(curr)
            for neighbor in get_neighbor(curr):
                if neighbor not in blocks:
                    if is_inside_testing_zone(neighbor, min_x, max_x, min_y, max_y, min_z, max_z):
                        frontier.append(neighbor)
    return outside

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        blocks = [x.split(',') for x in f.read().splitlines()]

    # Convert to ints
    blocks = [(int(x), int(y), int(z)) for x, y, z in blocks]

    # Print min and max in each direction
    min_x = min([x for x, y, z in blocks])
    max_x = max([x for x, y, z in blocks])
    min_y = min([y for x, y, z in blocks])
    max_y = max([y for x, y, z in blocks])
    min_z = min([z for x, y, z in blocks])
    max_z = max([z for x, y, z in blocks])
    print(f"min_x = {min_x}, max_x = {max_x}", flush=True)
    print(f"min_y = {min_y}, max_y = {max_y}", flush=True)
    print(f"min_z = {min_z}, max_z = {max_z}", flush=True)


    outside = get_outside(blocks, min_x, max_x, min_y, max_y, min_z, max_z)
    print(f"Outside: {len(outside)}", flush=True)
    total_size = (max_x-min_x+1)*(max_y-min_y+1)*(max_z-min_z+1)
    print(f"Inside: {total_size-len(outside)}", flush=True)
    print(f"Total size: {total_size}", flush=True)


    # For all blocks, check how many sides are exposed
    total = 0
    for x, y, z in blocks:
        for i in range(-1, 2, 2):
            if (x+i, y, z) not in blocks:
                if (x+i, y, z) in outside:
                    total += 1
            if (x, y+i, z) not in blocks:
                if (x, y+i, z) in outside:
                    total += 1
            if (x, y, z+i) not in blocks:
                if (x, y, z+i) in outside:
                    total += 1

    print(total)