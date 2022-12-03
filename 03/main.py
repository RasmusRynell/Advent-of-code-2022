import os
import json
from functools import reduce

def cnv(chr):
    if chr.islower():
        return abs(ord(chr)) - 96
    return abs(ord(chr)) - 38

def find_common_letters(strings):
    def single(string1, string2):
        return ''.join([x for x in string1 if x in string2])
    return reduce(single, strings)[0]


if __name__ == "__main__":
    total_sum_part1 = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            first_half = line[:len(line)//2]
            second_half = line[len(line)//2:]
            total_sum_part1 += cnv(find_common_letters([first_half, second_half]))

    print(f"Part 1: {total_sum_part1}")


    total_sum_part2 = 0
    strings = []
    with open('input.txt', 'r') as f:
        for curr_iter, line in enumerate(f):
            strings.append(line.replace('\n', ''))
            
            if (curr_iter+1) % 3 == 0:
                total_sum_part2 += cnv(find_common_letters(strings))
                strings = []

    print(f"Part 2: {total_sum_part2}")

