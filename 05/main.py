import os
import json

stacks_p1 = []
stacks_p2 = []

if __name__ == "__main__":
    
    is_in_beginning = True
    with open('input.txt', 'r') as f:
        for line in f:

            if is_in_beginning:
                if line != '\n':
                    # Split on each 4th character
                    line_list = [line[i+1:i+2] for i in range(0, len(line), 4)]

                    for idx, char in enumerate(line_list):
                        if len(stacks_p1) <= idx:
                            stacks_p1.append([])
                            stacks_p2.append([])
                        if char != ' ' and not char.isdigit():
                            stacks_p1[idx].append(char)
                            stacks_p2[idx].append(char)
                else:
                    # Reverse every stack ans save
                    stacks_p1 = [stack[::-1] for stack in stacks_p1]
                    stacks_p2 = [stack[::-1] for stack in stacks_p2]
                    is_in_beginning = False

            else:
                # Split on space
                line_list = line.split(' ')
                num_to_move = int(line_list[1])
                from_stack = int(line_list[3])-1
                to_stack = int(line_list[5])-1

                for _ in range(num_to_move):
                    stacks_p1[to_stack].append(stacks_p1[from_stack].pop())

                # Move num_to_move from from_stack to to_stack at once
                stacks_p2[to_stack] += stacks_p2[from_stack][-num_to_move:]
                stacks_p2[from_stack] = stacks_p2[from_stack][:-num_to_move]
            
        print(''.join([stack[-1] for stack in stacks_p1]))
        print(''.join([stack[-1] for stack in stacks_p2]))