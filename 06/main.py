import os
import json


def check(data, num_in_a_row):
    for idx, char in enumerate(data):
        if idx >= num_in_a_row:
            if len(set(data[idx-num_in_a_row:idx])) == num_in_a_row:
                return idx

if __name__ == "__main__":
    
    with open('input.txt', 'r') as f:
        data = f.read()

    print(f'Part 1: {check(data, 4)}')
    print(f'Part 2: {check(data, 14)}')