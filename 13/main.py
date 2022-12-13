import json
import sys
import os


def compare_packets(packet1, packet2):
    if type(packet1) is not list or type(packet2) is not list:
        print(f"Djud you got and error here: {packet1} vs {packet2}")
        return False

    idx_1 = 0
    idx_2 = 0
    while idx_1 < len(packet1) and idx_2 < len(packet2):
        print(f"\t- Compare {packet1[idx_1]} vs {packet2[idx_2]}", flush=True)
        
        if type(packet1[idx_1]) is int:
            if type(packet2[idx_2]) is int:
                if packet1[idx_1] < packet2[idx_2]:
                    print("\t\t- Left side is smaller, so inputs are in the right order (int,int)", flush=True)
                    return True
                    
                elif packet1[idx_1] > packet2[idx_2]:
                    print("\t\t- Right side is smaller, so inputs are in the wrong order (int,int)", flush=True)
                    return False
        
        if type(packet1[idx_1]) is list:
            if type(packet2[idx_2]) is list:
                if not compare_packets(packet1[idx_1], packet2[idx_2]):
                    return False
            else:
                if not compare_packets(packet1[idx_1], [packet2[idx_2]]):
                    return False

        elif type(packet2[idx_2]) is list:
            if not compare_packets([packet1[idx_1]], packet2[idx_2]):
                return False

        idx_1 += 1
        idx_2 += 1

    if idx_2 < len(packet2):
        print("- Left side ran out of items, so inputs are in the right order")
        return True
    elif idx_1 < len(packet1):
        print("- Right side ran out of items, so inputs are in the wrong order")
        return False
    return True

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input_test.txt'), 'r') as f:
        data = f.read().split('\n\n')

        correct = []
        for pair_idx, pair_of_packets in enumerate(data):
            print(f"== Pair {pair_idx+1} ==", flush=True)
            (packet1, packet2) = pair_of_packets.split('\n')
            packet1 = eval(packet1)
            packet2 = eval(packet2)

            print(f"- Compare {packet1} vs {packet2}", flush=True)

            if compare_packets(packet1, packet2):
                correct.append(pair_idx+1)
            
            print()

    print(f"Correct: {correct}, sum: {sum(correct)}", flush=True)