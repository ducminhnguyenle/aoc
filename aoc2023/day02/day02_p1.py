# Part 1
bag = {"red": 12,
       "green": 13,
       "blue": 14}

with open("day02_input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]
    
    result_p1 = 0
    for line in input:
        possible = True
        id, events = line.split(":")
        
        for event in events.split(";"):
            
            for collection in event.split(","):
                n, color = collection.split()
                if int(n) > bag.get(color, 0):
                    possible = False
        if possible:
            result_p1 += int(id.split()[-1])
            
    print(result_p1)