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
    for x,y in rock:
        new_x = x+stream
        if not (new_x < 7 and new_x >= 0):
            return rock
        string = (y,new_x)
        if string in stack and stack[string] != 0:
            return rock
    return [[x+stream,y] for x,y in rock]


def move_down(rock):
    for x,y in rock:
        string = (y-1,x)
        if string in stack and stack[string] != 0:
            return rock
    return [[x,y-1] for x,y in rock]


def are_same(half, top_y):
    for y in range(top_y-1, top_y-1-half, -1):
        for x in range(0, 7):
            string1 = (y,x)
            string2 = (y+half, x)
            # If both strings are in the stack
            if string1 in stack and string2 in stack:
                if stack[string1] != stack[string2]:
                    return False
            # If only one string is in the stack
            elif string1 in stack or string2 in stack:
                return False
    return True


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        jet_stream = f.read()

    # In jet stream convert '>' into 1 and '<' into -1
    jet_stream = [1 if x == '>' else -1 for x in jet_stream]

    stack = {}

    push_rock_times = []
    move_rock_down_times = []

    top_y = -1

    start = time.time()
    j = 0
    time_steps = 10_000_0#2022
    for i in range(0, time_steps):
        x = 2
        y = top_y + 4

        #print(x, y, flush=True)
        current_rock_char = rocks[i%len(rocks)]
        current_rock = make_rock(current_rock_char, x, y)

        while True:
            current_stream = jet_stream[j%len(jet_stream)]
            j += 1

            # Move rock side to side
            #print(f"Rock pushed {current_stream}", flush=True)
            timer3 = time.time()
            current_rock = push_rock(current_rock, current_stream)
            push_rock_times.append(time.time() - timer3)
            # Move rock down
            timer4 = time.time()
            old_curr = current_rock
            if y != 0:
                current_rock = move_down(current_rock)
                y -= 1
            move_rock_down_times.append(time.time() - timer4)

            if current_rock == old_curr:
                # Rock is at the bottom
                # Add rock to stack
                for x,y in current_rock:
                    stack[(y, x)] = rocks.index(current_rock_char) + 1
                    if y > top_y:
                        top_y = y
                break

        # Find if pattern repeats
        if top_y > 2:
            if are_same(top_y//2, top_y):
                print("Repeats", flush=True)

                # Print stack
                for y in range(0, top_y+1):
                    for x in range(0, 7):
                        string = (y,x)
                        if string in stack:
                            print(stack[string], end='')
                        else:
                            print(' ', end='')
                    print()
                break

    full_time = time.time() - start

    print("\n\n\n\nStats:")

    # Current height of stack
    print(f"Stack height: {top_y+1}", flush=True)
    print(f"Total time:\t\t {full_time*1000}ms", flush=True)
    print()

    # Print avr time all in ms
    print(f"Push rock left, right:\t {sum(push_rock_times)*1000:.4f}ms, {len(push_rock_times)}", flush=True)
    print(f"Move rock down:\t\t {sum(move_rock_down_times)*1000:.4f}ms, {len(move_rock_down_times)}", flush=True)
    total_sum = sum(push_rock_times)*1000 + sum(move_rock_down_times)*1000
    print(f"Sum: \t\t\t {total_sum:.4f}ms", flush=True)
    print(f"% of time:\t\t {total_sum/(full_time*1000)*100:.4f}%", flush=True)
    print()

    # Same thing but relative to time_steps
    print(f"Push rock left, right:\t {sum(push_rock_times)*1000/time_steps:.4f}ms", flush=True)
    print(f"Move rock down:\t\t {sum(move_rock_down_times)*1000/time_steps:.4f}ms", flush=True)
    print(f"Sum: \t\t\t {(sum(push_rock_times)*1000 + sum(move_rock_down_times)*1000)/time_steps:.4f}ms", flush=True)
    print(f"Total time:\t\t {full_time*1000/time_steps}ms", flush=True)



    print(f"\nTotal time:\t\t {full_time}s", flush=True)

    # Running this for 1000000000000 iterations instead of time_steps will take ... hours
    seconds = full_time * 1000000000000 / time_steps
    print(f"\nTime to run part2:\t {seconds/60/60:.2f}h", flush=True)