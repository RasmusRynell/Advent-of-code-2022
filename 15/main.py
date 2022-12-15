import json
import sys
import os
#import torch
import matplotlib.pyplot as plt
import time

plt.gca().invert_yaxis()

if __name__ == "__main__":
    cords = []
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().split('\n')
        for line in data:
            line_split = line.split(' ')
            sensor_x = line_split[2][2:-1]
            sensor_y = line_split[3][2:-1]
            beacon_x = line_split[8][2:-1]
            beacon_y = line_split[9][2:]
           # print(f"Sensor: ({sensor_x}, {sensor_y}) Beacon: ({beacon_x}, {beacon_y})")
            cords.append(((int(sensor_x), int(sensor_y)), (int(beacon_x), int(beacon_y))))

    #print(cords)

    occupied = {}

    # Show all ticks
    plt.xticks(range(-50, 50, 1))
    plt.yticks(range(-50, 50, 1))

    # Add grid
    plt.grid()

    i = 0
    # Plot top left is (0, 0)
    for sensor, beacon in cords:
        start = time.time()
        print(f"Sensor: {sensor} Beacon: {beacon}, {i}/{len(cords)}", flush=True)
        # Around each sensor plot a circle
        manhattan_distance_x = abs(sensor[0]-beacon[0])
        manhattan_distance_y = abs(sensor[1]-beacon[1])
        manhattan_distance = manhattan_distance_x + manhattan_distance_y
        #print(sensor, beacon, manhattan_distance_x, manhattan_distance_y, manhattan_distance_x+manhattan_distance_y, flush=True)
        # Plot points around sensor
        #print(f"{sensor[0]-manhattan_distance}, {sensor[0]+manhattan_distance+1}, {sensor[1]-manhattan_distance}, {sensor[1]+manhattan_distance+1}", flush=True)
        for x in range(sensor[0]-manhattan_distance, sensor[0]+manhattan_distance+1):
            for y in range(sensor[1]-manhattan_distance, sensor[1]+manhattan_distance+1):
                if abs(x-sensor[0]) + abs(y-sensor[1]) <= manhattan_distance:
                    if (x, y) not in occupied:
                        #occupied.append((x, y))
                        occupied[(x, y)] = 1
            print(f"{x}/{sensor[0]+manhattan_distance+1}", flush=True)
        print(f"Time: {time.time()-start}", flush=True)
        print(f"Done {i}/{len(cords)}", flush=True)
        i += 1

    # If any sensor or beacon is occupied, remove it
    for sensor, beacon in cords:
        if sensor in occupied:
            del occupied[sensor]
        if beacon in occupied:
            del occupied[beacon]

    # Plot all occupied points in black
    for x, y in occupied:
        plt.plot(x, y, 'ko')

    want_y = 10
    # Count how many points are occupied on y = want_y
    n = 0
    points_on_y = []
    for x, y in occupied:
        if y == want_y and (x, y) not in points_on_y:
            n += 1
            points_on_y.append((x, y))

    print(f"Number of points occupied on y = {want_y}: {n}", flush=True)

    for sensor, beacon in cords:
        # Plot sensor in red, beacon in blue and a line between them
        plt.plot(sensor[0], sensor[1], 'ro')
        plt.plot(beacon[0], beacon[1], 'bo')
        plt.plot([sensor[0], beacon[0]], [sensor[1], beacon[1]], 'k-')



    print(len('#########S#######S#'), flush=True)


    plt.show()