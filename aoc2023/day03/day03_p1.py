# Part 1
with open("./day03/day03_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    
# Number of lines:
n = len(lines)
# Number of characters in a line (all lines have same length):
m = len(lines[0])

def is_symbol(i: int, j: int):
    if not (0 <= i < n and 0<= j < m):
        return False
    
    return lines[i][j] != "." and not lines[i][j].isdigit()

result = 0
for i, line in enumerate(lines):
    start = 0
    j = 0
    # Find all numbers in the input
    while j < m:
        start = j
        num = ""
        while j < m and line[j].isdigit():
            num += line[j]
            j += 1
        
        if num == "":
            j += 1
            continue
        # Convert str back to int
        num = int(num)
        
        # Check left-side and right-side of each number:
        if is_symbol(i, start-1) or is_symbol(i, j):
            result += num
            continue
        # Check above row and the lower row including top left-right and bottom left-right of each number:
        for k in range(start-1, j+1):
            if is_symbol(i-1, k) or is_symbol(i+1, k):
                result += num
                break

print(result)