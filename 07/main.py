import json
import sys

working_dir_history = []
root = {
    '/': {
        'name': '/',
        'dirs': {},
        'files': [],
        'total_size': 0
    }
}

def add_dir(name, working_dir_history, current_dir):
    if len(working_dir_history) == 1:
        if name not in current_dir[working_dir_history[-1]]['dirs']:
            current_dir[working_dir_history[-1]]['dirs'][name] = {
                'name': name,
                'dirs': {},
                'files': [],
                'total_size': 0
            }
        else:
            print('Directory already exists, this is not allowed')
    else:
        add_dir(name, working_dir_history[1:], current_dir[working_dir_history[0]]['dirs'])

def add_file(name, size, working_dir_history, root):
    if len(working_dir_history) == 1:
        root[working_dir_history[-1]]['files'].append({
            'name': name,
            'size': size
        })
        root[working_dir_history[-1]]['total_size'] += size
        return size
    added_size = add_file(name, size, working_dir_history[1:], root[working_dir_history[0]]['dirs'])
    root[working_dir_history[0]]['total_size'] += added_size
    return added_size

def get_sizes(dir):
    result = []
    for (key, value) in dir.items():
        result.append((key, value['total_size']))
        result.extend(get_sizes(value['dirs']))
    return result

if __name__ == "__main__":
    
    with open('input.txt', 'r') as f:
        for line in f:
            if line[0] == '$':
                if line[2:4] == 'cd':
                    current_dir = line[5:-1]

                    if current_dir == '..':
                        working_dir_history.pop()
                    else:
                        working_dir_history.append(current_dir)

            else:
                if line[0:3] == 'dir':
                    name = line.split()[1]
                    add_dir(name, working_dir_history, root)

                else:
                    size, name = line.split()
                    size = int(size)
                    _ = add_file(name, size, working_dir_history, root)



    # Get all dirs with a total size under 100_000, add the sizes together
    sizes = get_sizes(root)
    total_size = 0
    for (key, value) in sizes:
        if value < 100_000:
            total_size += value
    print(total_size)
    
    root_space = root['/']['total_size']
    total_have = 70_000_000 - root_space
    total_needed = 30_000_000 - total_have
    print(f'Root space: {root_space}')
    print(f'Total have: {total_have}')
    print(f'Total needed: {total_needed}')

    # Sort on size
    sizes.sort(key=lambda x: x[1], reverse=False)
    # Find the smallest one over total_needed
    for (key, value) in sizes:
        if value > total_needed:
            print(f'Found: {key} {value}')
            break

    #print(json.dumps(root, indent=4))