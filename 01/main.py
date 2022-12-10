import os

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().split("\n\n") # Split into individual elves 
        data = [sum([int(y) for y in x.split("\n")]) for x in data] # Sum for each elf
        data.sort(key=lambda x: x, reverse=True)
        
        print(data[0])
        print(sum(data[0:3]))