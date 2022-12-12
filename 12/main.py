import json
import sys
import os
import torch
import matplotlib.pyplot as plt

full_map = []

def search(full_map, start, end, reverse=False):
    width = full_map.shape[1]
    height = full_map.shape[0]

    def is_valid_neighbor(curr_node, next_node):
        if (next_node[0] >= 0 and next_node[0] < width) and (next_node[1] >= 0 and next_node[1] < height):
            if reverse:
                if full_map[curr_node[1], curr_node[0]] - full_map[next_node[1], next_node[0]] <= 1:
                    return True
            else:
                if full_map[next_node[1], next_node[0]] - full_map[curr_node[1], curr_node[0]] <= 1:
                    return True
        return False


    def find_neighbors(node):
        neighbors = []
        if is_valid_neighbor(node, (node[0]-1, node[1])):
            neighbors.append((node[0]-1, node[1]))
        if is_valid_neighbor(node, (node[0]+1, node[1])):
            neighbors.append((node[0]+1, node[1]))
        if is_valid_neighbor(node, (node[0], node[1]-1)):
            neighbors.append((node[0], node[1]-1))
        if is_valid_neighbor(node, (node[0], node[1]+1)):
            neighbors.append((node[0], node[1]+1))
        return neighbors

    print(end)
    print(start)

    # Breadth first search
    queue = [start]
    parent = {start: None}
    while queue:
        curr_node = queue.pop(0)
        for neighbor in find_neighbors(curr_node):
            if neighbor not in parent:
                queue.append(neighbor)
                parent[neighbor] = curr_node
                if neighbor in end:
                    real_end = neighbor
                    # Break out of all loops
                    queue = []
                    break

    # Find the path
    best_path = [real_end]
    curr_node = real_end
    while curr_node != start:
        curr_node = parent[curr_node]
        best_path.append(curr_node)
    best_path.reverse()

    # Convert keys to strings and print
    parent = {str(k): str(v) for k, v in parent.items()}
    print(json.dumps(parent, indent=4))

    return best_path


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().split('\n')
        for y, row in enumerate(data):
            full_map.append([])
            for x, char in enumerate(row):
                if char == 'S':
                    start_node = (x, y)
                    full_map[y].append(ord('a')-97)
                elif char == 'E':
                    end_node = (x, y)
                    full_map[y].append(ord('z')-97)
                else:
                    full_map[y].append(ord(char)-97)

    # make into tensor
    full_map = torch.tensor(full_map)
    print(f"Start node: {start_node}, value={full_map[start_node[1],start_node[0]]}", flush=True)
    print(f"End node: {end_node}, value={full_map[end_node[1],end_node[0]]}", flush=True)

    end_nodes = []
    for y, row in enumerate(full_map):
        for x, val in enumerate(row):
            if val == 0:
                end_nodes.append((x, y))
                
    best_paths = [
        search(full_map, start_node, [end_node]),
        search(full_map, end_node, end_nodes, reverse=True),
    ]

    # Reverse (x, y) to (y, x)
    for path in best_paths:
        for i, node in enumerate(path):
            path[i] = (node[1], node[0])

    # Plot the map
    plt.imshow(full_map)

    # Plot the paths
    for i in range(len(best_paths)):
        x = [x[0] for x in best_paths[i]]
        y = [x[1] for x in best_paths[i]]
        plt.plot(y, x, 'r-' if i == 0 else 'b-')
    
        print(f"Part {i+1} len: {len(best_paths[i])-1}", flush=True)

    plt.show()