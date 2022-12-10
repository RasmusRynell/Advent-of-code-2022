import os

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().split("\n\n") # Split into groups
        data = [x.split("\n") for x in data] # Split into lines
        data = [[int(y) for y in x] for x in data] # Convert to ints
        data.sort(key=lambda x: sum(x), reverse=True) # Sort by sum
        
        print(sum(data[0])) # Print sum of first group
        print(sum(data[0]) + sum(data[1]) + sum(data[2])) # Print sum of first 3 groups