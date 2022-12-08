import json
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch

def get_view_distance(tensor_map, row_index, col_index):
    view_distance_right = 0
    view_distance_left = 0
    view_distance_up = 0
    view_distance_down = 0

    curr_max = tensor_map[row_index][col_index]
    
    # check up
    for i in range(row_index - 1, -1, -1):
        view_distance_up += 1
        if tensor_map[i][col_index] >= curr_max:
            break

    # check down
    for i in range(row_index + 1, tensor_map.shape[0]):
        view_distance_down += 1
        if tensor_map[i][col_index] >= curr_max:
            break

    # check left
    for i in range(col_index - 1, -1, -1):
        view_distance_left += 1
        if tensor_map[row_index][i] >= curr_max:
            break

    # check right
    for i in range(col_index + 1, tensor_map.shape[1]):
        view_distance_right += 1
        if tensor_map[row_index][i] >= curr_max:
            break

    return view_distance_right * view_distance_left * view_distance_up * view_distance_down


if __name__ == "__main__":
    
    # Read the input
    with open('input.txt', 'r') as f:
        data = f.read()
    
    # Split on newlines
    data = data.split('\n')

    # Convert all strings to ints
    data = [[int(d) for d in d] for d in [list(d) for d in data]]

    tensor = torch.tensor(data)
    print(tensor.shape)

    # Create a tensor of 0s
    plot_tensor = torch.zeros(tensor.shape[0], tensor.shape[1])

    can_be_seen = []
    max_rows = tensor.shape[0]
    max_cols = tensor.shape[1]


    for row_index in range(max_rows):
        largest_from_left = -1
        largest_from_right = -1
        largest_from_top = -1
        largest_from_bottom = -1
        for col_index in range(max_cols):
            # Update largest from left
            if tensor[row_index][col_index] > largest_from_left:
                largest_from_left = tensor[row_index][col_index]
                if (row_index,col_index) not in can_be_seen:
                    can_be_seen.append((row_index,col_index))
                    plot_tensor[row_index][col_index] = 1
            
            # Update largest from right
            if tensor[row_index][max_cols - col_index - 1] > largest_from_right:
                largest_from_right = tensor[row_index][max_cols - col_index - 1]
                if (row_index,max_cols - col_index - 1) not in can_be_seen:
                    can_be_seen.append((row_index, max_cols - col_index - 1))
                    plot_tensor[row_index][max_cols - col_index - 1] = 1
            
            # Update largest from top
            if tensor[col_index][row_index] > largest_from_top:
                largest_from_top = tensor[col_index][row_index]
                if (col_index,row_index) not in can_be_seen:
                    can_be_seen.append((col_index,row_index))
                    plot_tensor[col_index][row_index] = 1
            
            # Update largest from bottom
            if tensor[max_cols - col_index - 1][row_index] > largest_from_bottom:
                largest_from_bottom = tensor[max_cols - col_index - 1][row_index]
                if (max_cols - col_index - 1,row_index) not in can_be_seen:
                    can_be_seen.append((max_cols - col_index - 1,row_index))
                    plot_tensor[max_cols - col_index - 1][row_index] = 1

    print(len(can_be_seen), flush=True)
    plt.imshow(plot_tensor)
    plt.show()


    max_view_distance = 0
    view_distance_plot = torch.zeros(tensor.shape[0], tensor.shape[1])
    for row_index in range(max_rows):
        for col_index in range(max_cols):
            curr_distance = get_view_distance(tensor, row_index, col_index)
            view_distance_plot[row_index][col_index] = curr_distance
            if max_view_distance < curr_distance:
                max_view_distance = curr_distance

    

    print(max_view_distance, flush=True)

    
    plt.imshow(view_distance_plot)
    plt.show()
