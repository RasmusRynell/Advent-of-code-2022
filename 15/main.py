import json
import sys
import os
#import torch
import matplotlib.pyplot as plt
import time

plt.gca().invert_yaxis()

def is_close_enough(pos, cords):
    for sensor, beacon, manhattan in cords:
        if abs(test[0]-sensor[0]) + abs(test[1]-sensor[1]) <= manhattan:
            # If not a sensor or beacon
            if test != sensor and test != beacon:
                return True
                # # Plot green
                # plt.scatter(test[0], test[1], color='green')
                # n += 1
                # break
    return False

if __name__ == "__main__":
    cords = []
    with open(os.path.join(os.path.dirname(__file__), 'input_test.txt'), 'r') as f:
        data = f.read().split('\n')
        for line in data:
            line_split = line.split(' ')
            sensor_x = line_split[2][2:-1]
            sensor_y = line_split[3][2:-1]
            beacon_x = line_split[8][2:-1]
            beacon_y = line_split[9][2:]
           # print(f"Sensor: ({sensor_x}, {sensor_y}) Beacon: ({beacon_x}, {beacon_y})")
            cords.append(((int(sensor_x), int(sensor_y)), (int(beacon_x), int(beacon_y))))


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

        # Plot sensor and beacon red and blue
        plt.scatter(sensor[0], sensor[1], color='red')
        plt.scatter(beacon[0], beacon[1], color='blue')

        top = (sensor[0], sensor[1] + manhattan)
        bottom = (sensor[0], sensor[1] - manhattan)
        left = (sensor[0] - manhattan, sensor[1])
        right = (sensor[0] + manhattan, sensor[1])

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

    want_y = 10#2000000
    start = time.time()
    n = 0
    # For each x on y = want_y
    for x in range(-50, 50, 1):
    #for x in range(-5_000_000, 5_000_000, 1):
        test = (x, want_y)
        # If close enough to a sensor
        if is_close_enough(test, cords):
            # Plot green
            plt.scatter(test[0], test[1], color='green')
            n += 1


    print(f"n: {n}", flush=True)

    plt.show()
