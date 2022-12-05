import os
import json










stacks = []

if __name__ == "__main__":
    
    is_in_beginning = True
    with open('input.txt', 'r') as f:
        for line in f:

            if is_in_beginning:
                if line != '\n':
                    # Split on each 4th character
                    line_list = [line[i+1:i+2] for i in range(0, len(line), 4)]

                    for idx, char in enumerate(line_list):
                        if len(stacks) <= idx:
                            stacks.append([])
                        if char != ' ' and not char.isdigit():
                            stacks[idx].append(char)
                else:
                    # Reverse every stack ans save
                    stacks = [stack[::-1] for stack in stacks]
                    is_in_beginning = False

            else:
                # Split on space
                line_list = line.split(' ')
                num_to_move = int(line_list[1])
                from_stack = int(line_list[3])-1
                to_stack = int(line_list[5])-1

                for _ in range(num_to_move):
                    stacks[to_stack].append(stacks[from_stack].pop())
            
        # Get each last element of each stack
        print(''.join([stack[-1] for stack in stacks]))