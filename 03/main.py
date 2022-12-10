import os
import json
from functools import reduce

def cnv(chr):
    if chr.islower():
        return abs(ord(chr)) - 96
    return abs(ord(chr)) - 38

def find_common_letters(strings):
    return reduce(lambda string1, string2: ''.join([x for x in string1 if x in string2]), strings)[0]


if __name__ == "__main__":
    total_sum_part1 = 0
    total_sum_part2 = 0
    all_strings = []
    
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        for idx, line in enumerate(f):
            line = line.strip()
            all_strings.append(line)
            first_half = line[:len(line)//2]
            second_half = line[len(line)//2:]

            total_sum_part1 += cnv(find_common_letters([first_half, second_half]))
            
            if (idx+1) % 3 == 0:
                total_sum_part2 += cnv(find_common_letters(all_strings[-3:]))

    print(f"Part 1: {total_sum_part1}")
    print(f"Part 2: {total_sum_part2}")

