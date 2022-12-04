import os
import json

def overlap(a_start, a_end, b_start, b_end):
    if (a_start <= b_start <= a_end) or \
       (a_start <= b_end <= a_end) or \
       (b_start <= a_start <= b_end) or \
       (b_start <= a_end <= b_end):
        return True
    return False

def fully_contained(a_start, a_end, b_start, b_end):
    if (a_start <= b_start <= b_end <= a_end):
        return True
    return False

if __name__ == "__main__":
    
    total_part1 = 0
    total_part2 = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            pairs = line.split(",")
            a_range_start, a_range_end = pairs[0].split("-")
            b_range_start, b_range_end = pairs[1].split("-")

            if fully_contained(int(a_range_start), int(a_range_end), int(b_range_start), int(b_range_end)) or \
                fully_contained(int(b_range_start), int(b_range_end), int(a_range_start), int(a_range_end)):
                total_part1 += 1

            if overlap(int(a_range_start), int(a_range_end), int(b_range_start), int(b_range_end)):
                total_part2 += 1

    print(f"Part 1: {total_part1}")
    print(f"Part 2: {total_part2}")