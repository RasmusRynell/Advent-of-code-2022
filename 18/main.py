import json
import sys
import os
#import torch
import numpy as np
import matplotlib.pyplot as plt
import time

plt.ion()



if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        blocks = [x.split(',') for x in f.read().splitlines()]

    # Convert to ints
    blocks = [(int(x), int(y), int(z)) for x, y, z in blocks]

    # For all blocks, check how many sides are exposed
    total = 0
    for x, y, z in blocks:
        for i in range(-1, 2, 2):
            if (x+i, y, z) not in blocks:
                total += 1
            if (x, y+i, z) not in blocks:
                total += 1
            if (x, y, z+i) not in blocks:
                total += 1

    print(total)