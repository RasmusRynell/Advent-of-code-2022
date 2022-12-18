stack = [
    [0,0,0,0],
    [0,0,1,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,1,1,1],
]

stack2 = {}
for col in range(0, len(stack[0])):
    for row in range(0, len(stack)):
        if stack[row][col] != 0:
            stack2[(row, col)] = stack[row][col]
print(stack2)




def are_same(half, top_y):
    for y in range(top_y-1, top_y-1-half, -1):
        for x in range(0, 4):
            if stack[y][x] != stack[y-half][x]:
                return False
    return True

def repeats(stack, top_y):
    for i in range(1, top_y//2+1):
        if are_same(i, top_y):
            return True
    return False

def repeats2(stack, top_y):
    for i in range(1, top_y//2+1):
        print(f"i = {i}")
        if are_same2(i, top_y):
            return True
    return False

def are_same2(half, top_y):
    for y in range(top_y-1, top_y-1-half, -1):
        print(f"y = {y}, {y-half}")
        for x in range(0, 4):
            string1 = (y,x)
            string2 = (y-half, x)
            # If both strings are in the stack
            if string1 in stack and string2 in stack:
                if stack[string1] != stack[string2]:
                    print(f"{string1} {string2} = false")
                    return False
            # If only one string is in the stack
            elif string1 in stack or string2 in stack:
                print(f"{string1} {string2} = false")
                return False
            print(f"{string1} {string2} = true")
    return True

print(repeats(stack, len(stack)))
print(repeats2(stack2, len(stack)))

assert repeats(stack, len(stack)) == repeats2(stack2, len(stack))