# Part 2
with open("day03_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    
# Number of lines:
n = len(lines)
# Number of characters in a line (all lines have same length):
m = len(lines[0])

# Array contains number adjacent to "*" symbol 
arrs = [[[] for _ in range(m)] for _ in range(n)]

def is_symbol(i: int, j: int, num):
    if not (0 <= i < n and 0 <= j < m):
        return False
    # Check "*" symbol next to a number
    if lines[i][j] == "*":
      arrs[i][j].append(num)
      
    return lines[i][j] != "." and not lines[j][j].isdigit()  

for i, line in enumerate(lines):
    start = 0
    j = 0
    while j < m:
        start = j
        num = ""
        while j < m and line[j].isdigit():
            num += line[j]
            j += 1
        if num == "":
            j += 1
            continue
        num = int(num)
        
        # Number ended, look around
        is_symbol(i, start - 1, num) or is_symbol(i, j, num)
         
        for k in range(start - 1, j + 1):
            is_symbol(i - 1, k, num) or is_symbol(i + 1, k, num)

result = 0
for i in range(n):
    for j in range(m):
        nums = arrs[i][j]
        if len(nums) == 2 and lines[i][j] == "*":
            # print(nums)
            result += nums[0] * nums[1]
print(result)