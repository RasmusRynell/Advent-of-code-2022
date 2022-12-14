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
    min_y = 0
    for path in full_map:
        for x, y in path:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y

    print((min_x, min_y), (max_x, max_y), flush=True)
    print(f"Size: {max_x-min_x}x{max_y-min_y}", flush=True)

    # Create a zero tensor
    result = torch.zeros((max_y-min_y+1, max_x-min_x+1), dtype=torch.int8)

    #print(full_map, flush=True)

    for path in full_map:
        for idx, (x, y) in enumerate(path):
            if idx == 0:
                continue
            x1, y1 = path[idx-1]
            x2, y2 = path[idx]
            if x1 == x2:
                if y1 < y2:
                    result[y1-min_y:y2-min_y+1, x1-min_x] = 1
                else:
                    result[y2-min_y:y1-min_y+1, x1-min_x] = 1
            elif y1 == y2:
                if x1 < x2:
                    result[y1-min_y, x1-min_x:x2-min_x+1] = 1
                else:
                    result[y1-min_y, x2-min_x:x1-min_x+1] = 1
            else:
                raise Exception(f"Invalid path: {path}")

    # Sand source
    result[0, 500-min_x] = 2

    return result

def fall_sand(current_map, n):

    sand_has_fallen_off = False
    current_sand_pos = torch.where(current_map == 2)
    movement = []
    while True:
        # If can fall down
        if not (current_sand_pos[0]+1 == current_map.shape[0]) and \
            current_map[current_sand_pos[0]+1, current_sand_pos[1]] == 0:
                current_sand_pos = (current_sand_pos[0]+1, current_sand_pos[1])
                movement.append((current_sand_pos[0], current_sand_pos[1]))
    
        # Else if can fall down left
        elif not (current_sand_pos[0]+1 == current_map.shape[0]) and \
            not (current_sand_pos[1]-1 == -1) and \
            current_map[current_sand_pos[0]+1, current_sand_pos[1]-1] == 0:
                current_sand_pos = (current_sand_pos[0]+1, current_sand_pos[1]-1)
                movement.append((current_sand_pos[0], current_sand_pos[1]))

        # Else if can fall down right
        elif not (current_sand_pos[0]+1 == current_map.shape[0]) and \
            not (current_sand_pos[1]+1 == current_map.shape[1]) and \
            current_map[current_sand_pos[0]+1, current_sand_pos[1]+1] == 0:
                current_sand_pos = (current_sand_pos[0]+1, current_sand_pos[1]+1)
                movement.append((current_sand_pos[0], current_sand_pos[1]))

        else:
            break

    if current_sand_pos[0] == current_map.shape[0] or \
        current_sand_pos[1] == -1 or \
            current_sand_pos[1] == current_map.shape[1]:
        sand_has_fallen_off = True

    if not sand_has_fallen_off:
        current_map[current_sand_pos[0], current_sand_pos[1]] = 3
    else:
        for x, y in movement:
            current_map[x, y] = -1


    return current_map, sand_has_fallen_off

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().split('\n')

    current_map = create_map(data)

    n = 0
    sand_has_fallen_off = False
    while not sand_has_fallen_off:
        current_map, sand_has_fallen_off = fall_sand(current_map, n)

        #if n in [0, 1, 4, 21, 23]:
        #    print(f"Step {n}:")
        #    print(current_map, flush=True, end='\n\n')
        #    plt.imshow(current_map)
        #    plt.show()
        n += 1

    plt.imshow(current_map)
    plt.show()

    print(f"{n-1} units of sand comes to a rest before they stat falling off into the abyss", flush=True)

