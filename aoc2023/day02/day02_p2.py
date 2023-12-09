# Part 2
from collections import defaultdict

with open("day02_input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]
    
    result_p2 = 0
    for line in input:
        # Using defaultdict(int) class to avoid KeyError
        min_set = defaultdict(int)
        id, events = line.split(":")

        for event in events.split(";"):
            
            for collection in event.split(","):
                n, color = collection.split()
                # Keep the highest value, avoid overwritten
                min_set[color] = max(int(n), min_set[color])
        
        power = 1        
        for value in min_set.values():
            power *= value
        result_p2 += power
    
    print(result_p2)