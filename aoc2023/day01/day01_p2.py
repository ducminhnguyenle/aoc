# Part 2
num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open("day01_input.txt") as f:
    
    input = [line.strip() for line in f.readlines()]
    
    result = 0
    for line in input:
        fst = None
        lst = None
        s = ""
        
        for element in line:
            digit = None
            
            if element.isdigit():
                digit = element
            else:
                s += element
                for k,v in num.items():
                    if s.endswith(k):
                        digit = str(v)
            
            if digit is not None:
                lst = digit
                if fst is None:
                    fst = digit
        
        result += int(fst + lst)
        
    print(result)