import json
import sys
import os
#import torch
import matplotlib.pyplot as plt
import time

plt.gca().invert_yaxis()

def is_close_enough(pos, cords):
    for sensor, beacon, manhattan in cords:
        if abs(pos[0]-sensor[0]) + abs(pos[1]-sensor[1]) <= manhattan:
            return True
    return False

def read_data(file):
    cords = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as f:
        data = f.read().split('\n')
        for line in data:
            line_split = line.split(' ')
            sensor_x = line_split[2][2:-1]
            sensor_y = line_split[3][2:-1]
            beacon_x = line_split[8][2:-1]
            beacon_y = line_split[9][2:]
            cords.append(((int(sensor_x), int(sensor_y)), (int(beacon_x), int(beacon_y))))

    return cords

def part1(test):
    cords = read_data('input_test.txt' if test else 'input.txt')
    want_y = 10 if test else 2000000

    if test:
        # Show all ticks
        plt.xticks(range(-50, 50, 1))
        plt.yticks(range(-50, 50, 1))

        # Add grid
        plt.grid()

    
    
    # For each sensor and beacon plot things
    for idx, items in enumerate(cords):
        sensor, beacon = items
        # Find manhattan distance
        manhattan = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
        print(f"Sensor: {sensor} Beacon: {beacon} Manhattan: {manhattan}")


        top = (sensor[0], sensor[1] + manhattan)
        bottom = (sensor[0], sensor[1] - manhattan)
        left = (sensor[0] - manhattan, sensor[1])
        right = (sensor[0] + manhattan, sensor[1])

        if test:
            # Plot sensor and beacon red and blue
            plt.scatter(sensor[0], sensor[1], color='red')
            plt.scatter(beacon[0], beacon[1], color='blue')


            # Plot line between top->left,right, bottom->left,right, left->top,bottom, right->top,bottom
            plt.plot([top[0], left[0]], [top[1], left[1]], color='black')
            plt.plot([top[0], right[0]], [top[1], right[1]], color='black')
            plt.plot([bottom[0], left[0]], [bottom[1], left[1]], color='black')
            plt.plot([bottom[0], right[0]], [bottom[1], right[1]], color='black')
            plt.plot([left[0], top[0]], [left[1], top[1]], color='black')
            plt.plot([left[0], bottom[0]], [left[1], bottom[1]], color='black')
            plt.plot([right[0], top[0]], [right[1], top[1]], color='black')
            plt.plot([right[0], bottom[0]], [right[1], bottom[1]], color='black')

        cords[idx] = (sensor, beacon, manhattan)

    n = 0
    run_range = range(-50, 50, 1) if test else range(-5_000_000, 5_000_000, 1)
    for x in run_range:
        test = (x, want_y)
        if is_close_enough(test, cords):
            # Plot green
            if test:
                plt.scatter(test[0], test[1], color='green')
            n += 1


    print(f"n: {n}", flush=True)

    if test:
        plt.show()

def part2(test):
    cords = read_data('input_test.txt' if test else 'input.txt')
    
    check = 20 if test else 4000000
    if test:
        # Show all ticks
        plt.xticks(range(-50, 50, 1))
        plt.yticks(range(-50, 50, 1))

        # Add grid
        plt.grid()

    for idx, items in enumerate(cords):
        sensor, beacon = items
        manhattan = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])

        print(f"Sensor: {sensor} Beacon: {beacon} Manhattan: {manhattan}", flush=True)
        cords[idx] = (sensor, beacon, manhattan)

        top = (sensor[0], sensor[1] + manhattan)
        bottom = (sensor[0], sensor[1] - manhattan)
        left = (sensor[0] - manhattan, sensor[1])
        right = (sensor[0] + manhattan, sensor[1])

        if test:
            x = sensor[0]
            y = sensor[1]
            # Plot sensor and beacon red and blue
            plt.scatter(sensor[0], sensor[1], color='red')
            plt.scatter(beacon[0], beacon[1], color='blue')


            # Plot line between top->left,right, bottom->left,right, left->top,bottom, right->top,bottom
            plt.plot([top[0], left[0]], [top[1], left[1]], color='black')
            plt.plot([top[0], right[0]], [top[1], right[1]], color='black')
            plt.plot([bottom[0], left[0]], [bottom[1], left[1]], color='black')
            plt.plot([bottom[0], right[0]], [bottom[1], right[1]], color='black')
            plt.plot([left[0], top[0]], [left[1], top[1]], color='black')
            plt.plot([left[0], bottom[0]], [left[1], bottom[1]], color='black')
            plt.plot([right[0], top[0]], [right[1], top[1]], color='black')
            plt.plot([right[0], bottom[0]], [right[1], bottom[1]], color='black')

    total = len(cords)*(manhattan+2)*2*2
    print(f"Total: {total}", flush=True)

    for items in cords[::-1]:
        sensor, beacon, _ = items

        manhattan = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
        x = sensor[0]
        y = sensor[1]
        for i in range(0, manhattan + 2):
            for j in range(-1, 2, 2):
                for k in range(1, -2, -2):
                    new_x_1 = (x-(manhattan*j))+(i*k)-1
                    new_y_1 = y-i
                    if not(new_x_1 < 0 or new_x_1 > check or new_y_1 < 0 or new_y_1 > check):
                        if not is_close_enough((new_x_1, new_y_1), cords):
                            print(f"Frequency {(new_x_1*4000000)+new_y_1}", flush=True)
                            if test:
                                plt.scatter(new_x_1, new_y_1, color='green')
                            return
    if test:
        plt.show()

if __name__ == "__main__":
    #part1(False)
    
    start = time.time()
    part2(False)
    end = time.time()
    print(f"Time: {end-start}", flush=True)

