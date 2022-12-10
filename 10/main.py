import json
import sys


X = 1
cycle_values_of_X = [X]

width = 40
height = 6

def addx(V):
    global X, cycle_values_of_X
    cycle_values_of_X.append(X)
    X += V
    cycle_values_of_X.append(X)

def noop():
    global cycle, cycle_values_of_X
    cycle_values_of_X.append(X)

def draw(cycle_values_of_X):
    global width, height
    for i in range(height):
        for j in range(width):
            value = cycle_values_of_X[i * width + j]
            print('#' if (value-1 <= j <= value+1) else '.', end='')
        print()


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            line_list = line.split()
            instruction = line_list[0]
            
            if instruction == 'addx':
                addx(int(line_list[1]))
            elif instruction == 'noop':
                noop()

    total_sum = 0
    for idx in range(20, len(cycle_values_of_X), 40):
        total_sum += idx * cycle_values_of_X[idx - 1]

    print(f'Total sum: {total_sum}')
    draw(cycle_values_of_X)