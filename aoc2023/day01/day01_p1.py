# Part 1
with open("day01_input.txt", "r") as f:
    
    result = 0
    for line in f.readlines():
        fst = None
        lst = None
        
        for element in line:
            if element.isdigit():
                lst = element
                if fst is None:
                    fst = element
        result += int(fst + lst)
        
    print(result)       # 54081