import json
import sys
import os
#import torch
import matplotlib.pyplot as plt
import time

'''
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
'''


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input_test.txt'), 'r') as f:
        data = f.read().split('\n')
    data = [line.split(' ') for line in data]
    data = [(line[1], line[4][5:-1], [x.replace(",", "") for x in line[9:]]) for line in data]
    
    valves = {}
    for valve, flow, tunnels in data:
        valves[valve] = {'flow': int(flow), 'tunnels': tunnels, 'opened': False}

    start = 'AA'
    mins = 30

    # BFS
    queue = [(start, 0)]
    while queue:
        current, steps = queue.pop(0)
        if steps > mins:
            break
        if valves[current]['opened']:
            continue
        valves[current]['opened'] = True
        for tunnel in valves[current]['tunnels']:
            queue.append((tunnel, steps+1))

    print(sum([valve['flow'] for valve in valves.values() if valve['opened']]))
    