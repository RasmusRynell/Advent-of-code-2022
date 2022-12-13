import json
import sys
import os


def compare_packets(packet1, packet2):
    if isinstance(packet1, int) and isinstance(packet2, int):
        return -1 if packet1 < packet2 else 1 if packet2 < packet1 else 0 # -1 = ok, 0 = continue, 1 = not ok
    elif isinstance(packet1, int) and isinstance(packet2, list):
        return compare_packets([packet1], packet2)
    elif isinstance(packet1, list) and isinstance(packet2, int):
        return compare_packets(packet1, [packet2])
    
    if len(packet1) == 0 and len(packet2) != 0:
        return -1
    elif len(packet1) != 0 and len(packet2) == 0:
        return 1
    elif len(packet1) == 0 and len(packet2) == 0:
        return 0
    else:
        result = compare_packets(packet1[0], packet2[0])
        if result == 0:
            return compare_packets(packet1[1:], packet2[1:])
        return result
    return 0



if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input_test.txt'), 'r') as f:
        data = f.read().split('\n\n')
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data2 = f.read().split('\n\n')

    
    correct = []
    correct2 = []
    for pair_idx, pair_of_packets in enumerate(data):
        (packet1, packet2) = pair_of_packets.split('\n')
        if compare_packets(eval(packet1), eval(packet2)) == -1:
            correct.append(pair_idx+1)

    for pair_idx, pair_of_packets in enumerate(data2):
        (packet1, packet2) = pair_of_packets.split('\n')
        if compare_packets(eval(packet1), eval(packet2)) == -1:
            correct2.append(pair_idx+1)

    print(f"Correct: {correct}, sum: {sum(correct)}", flush=True)
    print(f"Correct2: {correct2}, sum: {sum(correct2)}", flush=True)


    temp = []
    for pair_of_packets in data2:
        (packet1, packet2) = pair_of_packets.split('\n')
        temp.append(eval(packet1))
        temp.append(eval(packet2))

    temp.append([[2]])
    temp.append([[6]])

    # Sort using compare_packets
    from functools import cmp_to_key
    temp.sort(key=cmp_to_key(compare_packets))
    
    index_for_2 = temp.index([[2]])+1
    index_for_6 = temp.index([[6]])+1

    print(f"decoder key: {index_for_2*index_for_6}")