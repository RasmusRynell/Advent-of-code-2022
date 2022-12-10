import os

p1 = {"A X": 3+1, "B X": 0+1, "C X": 6+1,
      "A Y": 6+2, "B Y": 3+2, "C Y": 0+2,
      "A Z": 0+3, "B Z": 6+3, "C Z": 3+3}

p2 = {"A X": 0+3, "B X": 0+1, "C X": 0+2,
      "A Y": 3+1, "B Y": 3+2, "C Y": 3+3,
      "A Z": 6+2, "B Z": 6+3, "C Z": 6+1}

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        print(f'Part1: {sum([p1[line[0:3]] for line in f])}')
        print(f'Part2: {sum([p2[line[0:3]] for line in f])}')