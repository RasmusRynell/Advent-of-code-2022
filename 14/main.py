import json
import sys
import os
import torch
import matplotlib.pyplot as plt


def create_map(data):
    full_map = []

    for path in data:
        full_map.append([])
        cords = path.split(' -> ')
        for cord in cords:
            x, y = cord.split(',')
            full_map[-1].append((int(x), int(y)))

    max_x = full_map[0][0][0]
    max_y = full_map[0][0][1]
    min_x = full_map[0][0][0]
    for path in full_map:
        for x, y in path:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            if x < min_x:
                min_x = x


    full_map.append([(0, max_y+2), (1000, max_y+2)])

    print(full_map, flush=True)

    # Create a zero tensor
    result = torch.zeros((max_y+3, 1000), dtype=torch.int8)
    print(result.shape, flush=True)

    for path in full_map:
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

    # Sand source
    result[0, 500] = 2

    return result, (min_x, 0), (max_x, max_y)

def is_outside_map(current_map, pos, border):
    return pos[0] == border[2] or \
        pos[1] == border[0] or \
            pos[1] == border[1]

def get_new_pos(current_map, current_pos, border):
    # If we can go down
    if is_outside_map(current_map, (current_pos[0]+1, current_pos[1]), border) or current_map[current_pos[0]+1, current_pos[1]] == 0:
        # If it is open return the old pos
        if is_outside_map(current_map, (current_pos[0]+1, current_pos[1]), border):
            return current_pos, True
        return (current_pos[0]+1, current_pos[1]), False

    # If we can go down left
    if is_outside_map(current_map, (current_pos[0]+1, current_pos[1]-1), border) or current_map[current_pos[0]+1, current_pos[1]-1] == 0:
        # If it is open return the old pos
        if is_outside_map(current_map, (current_pos[0]+1, current_pos[1]-1), border):
            return current_pos, True
        return (current_pos[0]+1, current_pos[1]-1), False

    # If we can go down right
    if is_outside_map(current_map, (current_pos[0]+1, current_pos[1]+1), border) or current_map[current_pos[0]+1, current_pos[1]+1] == 0:
        # If it is open return the old pos
        if is_outside_map(current_map, (current_pos[0]+1, current_pos[1]+1), border):
            return current_pos, True
        return (current_pos[0]+1, current_pos[1]+1), False

    if  is_outside_map(current_map, (current_pos[0]-1, current_pos[1]), border):
        return current_pos, True

    return current_pos, False


def fall_sand(current_map, border, movement):

    has_fallen_off = False
    
    spawn = torch.where(current_map == 2)
    spawn_pos = (spawn[0][0], spawn[1][0])
    current_pos = spawn_pos if len(movement) == 0 else movement.pop()
    
    #print(f"Started with movement: {movement}")

    while True:
        new_pos, has_fallen_off = get_new_pos(current_map, current_pos, border)
        #print(f"Current pos: {current_pos}, new pos: {new_pos}", flush=True)
        if new_pos == current_pos:
            #print("No new pos", flush=True)
            if new_pos == spawn_pos:
                has_fallen_off = True
            break
        movement.append(new_pos)
        current_pos = new_pos

    if not has_fallen_off:
        current_map[current_pos[0], current_pos[1]] = 3
    else:
        for x, y in movement:
            current_map[x, y] = -1

    #print(f"Ended with movement: {movement[:-1]}")
    return current_map, has_fallen_off, movement[:-1]

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().split('\n')

    current_map, top_left, bottom_right = create_map(data)

    #border = (top_left[0]-1, bottom_right[0]+1, bottom_right[1]+1) # Part1
    border = (0, 1000, bottom_right[1]+3) # Part2

    plt.ion()
    map_plot = plt.imshow(current_map)

    movement = []
    n = 0
    sand_has_fallen_off = False
    while not sand_has_fallen_off:
        current_map, sand_has_fallen_off, movement = fall_sand(current_map, border, movement)
        n += 1
        map_plot.set_data(current_map)
        plt.draw()
        plt.pause(0.0001)

    print(f"{n-1} units of sand comes to a rest before they stat falling off into the abyss", flush=True)

    # Wait for user to close the plot
    plt.close()
    plt.ioff()


    plt.imshow(current_map)
    plt.show()

