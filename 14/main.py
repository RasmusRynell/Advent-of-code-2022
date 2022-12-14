import json
import sys
import os
import torch
import matplotlib.pyplot as plt
import time

def create_map(data):
    walls = []

    for path in data:
        walls.append([])
        cords = path.split(' -> ')
        for cord in cords:
            x, y = cord.split(',')
            walls[-1].append((int(x), int(y)))

    max_x = walls[0][0][0]
    max_y = walls[0][0][1]
    min_x = walls[0][0][0]
    for path in walls:
        for x, y in path:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            if x < min_x:
                min_x = x

    # Add floor for part 2
    walls.append([(0, max_y+2), (1000, max_y+2)])

    # Create a zero tensor
    result = torch.zeros((max_y+3, 1000), dtype=torch.int8)

    for path in walls:
        for idx, (x, y) in enumerate(path):
            if idx == 0:
                continue
            x1, y1 = path[idx-1]
            x2, y2 = path[idx]
            if x1 == x2:
                # Vertical line
                if y1 < y2:
                    result[y1:y2+1, x1] = 1
                else:
                    result[y2:y1+1, x1] = 1
            else:
                # Horizontal line
                if x1 < x2:
                    result[y1, x1:x2+1] = 1
                else:
                    result[y1, x2:x1+1] = 1

    # Add source
    result[0, 500] = 2

    return result, (min_x, 0), (max_x, max_y)

def is_outside_map(pos, border):
    global my_map
    return pos[0] == border[2] or \
        pos[1] == border[0] or \
            pos[1] == border[1]

def get_new_pos(current_pos, border):
    global my_map
    # If we can go down
    if is_outside_map((current_pos[0]+1, current_pos[1]), border) or my_map[current_pos[0]+1, current_pos[1]] == 0:
        # If it is open return the old pos
        if is_outside_map((current_pos[0]+1, current_pos[1]), border):
            return current_pos, True
        return (current_pos[0]+1, current_pos[1]), False

    # If we can go down left
    if is_outside_map((current_pos[0]+1, current_pos[1]-1), border) or my_map[current_pos[0]+1, current_pos[1]-1] == 0:
        # If it is open return the old pos
        if is_outside_map((current_pos[0]+1, current_pos[1]-1), border):
            return current_pos, True
        return (current_pos[0]+1, current_pos[1]-1), False

    # If we can go down right
    if is_outside_map((current_pos[0]+1, current_pos[1]+1), border) or my_map[current_pos[0]+1, current_pos[1]+1] == 0:
        # If it is open return the old pos
        if is_outside_map((current_pos[0]+1, current_pos[1]+1), border):
            return current_pos, True
        return (current_pos[0]+1, current_pos[1]+1), False

    if  is_outside_map((current_pos[0]-1, current_pos[1]), border):
        return current_pos, True

    return current_pos, False


def fall_sand(border, movement):
    global my_map

    has_fallen_off = False
    
    spawn = torch.where(my_map == 2)
    spawn_pos = (spawn[0][0], spawn[1][0])
    current_pos = spawn_pos if len(movement) == 0 else movement.pop()
    
    #print(f"Started with movement: {movement}")

    while True:
        new_pos, has_fallen_off = get_new_pos(current_pos, border)
        #print(f"Current pos: {current_pos}, new pos: {new_pos}", flush=True)
        if new_pos == current_pos:
            #print("No new pos", flush=True)
            if new_pos == spawn_pos:
                has_fallen_off = True
            break
        movement.append(new_pos)
        current_pos = new_pos

    if not has_fallen_off:
        my_map[current_pos[0], current_pos[1]] = 3
    else:
        for x, y in movement:
            my_map[x, y] = -1

    #print(f"Ended with movement: {movement[:-1]}")
    return has_fallen_off, movement[:-1]


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().split('\n')

    my_map, top_left, bottom_right = create_map(data)

    part = 2

    border = (top_left[0]-1, bottom_right[0]+1, bottom_right[1]+1) if part == 1 \
        else (0, 1000, bottom_right[1]+3)

    movement = []
    n = 0
    sand_has_fallen_off = False

    start = time.time()
    while not sand_has_fallen_off:
        sand_has_fallen_off, movement = fall_sand(border, movement)
        n += 1
    print(f"Time: {time.time()-start}", flush=True)

    print(f"{n-(1 if part == 1 else 0)} units of sand has come to rest", flush=True)

    # Wait for user to close the plot
    plt.close()
    plt.ioff()


    plt.imshow(my_map)
    plt.show()

