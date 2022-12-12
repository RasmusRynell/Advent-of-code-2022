import json
import sys
import os
import torch
import matplotlib.pyplot as plt

full_map = []

def search(full_map, start, end):
    # Start is a tuple of (x, y)
    # End is a tuple of (x, y)
    # full_map is a 2D tensor of integers

    width = full_map.shape[1]
    height = full_map.shape[0]

    def is_valid_neighbor(curr_node, next_node):
        if (next_node[0] >= 0 and next_node[0] < width) and (next_node[1] >= 0 and next_node[1] < height):
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
    
    # Breadth first search
    queue = [start]
    parent = {start: None}
    while queue:
        curr_node = queue.pop(0)
        if curr_node == end:
            print("Found the end node", flush=True)
            break
        for neighbor in find_neighbors(curr_node):
            print(f'\tparent[{curr_node}] added {curr_node}')
            if neighbor not in parent:
                queue.append(neighbor)
                parent[neighbor] = curr_node
    # Find the path
    best_path = [end]
    curr_node = end
    while curr_node != start:
        curr_node = parent[curr_node]
        best_path.append(curr_node)
    best_path.reverse()

    return best_path

def visualize_map(full_map, parent, start, end):
    # Plot the map
    plt.imshow(full_map)

    # Plot the path
    curr_node = end
    while curr_node != start:
        curr_node = parent[curr_node]
        plt.plot(curr_node[1], curr_node[0], 'r.')

    plt.show()

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

    #end_node = (156,8)

    # make into tensor
    full_map = torch.tensor(full_map)
    print(f"Start node: {start_node}, value={full_map[start_node[1],start_node[0]]}", flush=True)
    print(f"End node: {end_node}, value={full_map[end_node[1],end_node[0]]}", flush=True)

    # Search for the path
    best_path = search(full_map, start_node, end_node)
    #best_path = []
    print(best_path, flush=True)

    # Reverse (x, y) to (y, x)
    best_path = [(x[1], x[0]) for x in best_path]

    # Plot the map
    plt.imshow(full_map)

    # Plot the path
    x = [x[0] for x in best_path]
    y = [x[1] for x in best_path]
    plt.plot(y, x, 'r-')
    
    print(f"Length {len(best_path)-1}", flush=True)

    # Add text for start and end nodes
    plt.text(start_node[0], start_node[1], 'S', color='r')
    plt.text(end_node[0], end_node[1], 'E', color='r')


    plt.show()
