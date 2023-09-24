#AOC Day 17 2015
string = """50
44
11
49
42
46
18
32
26
40
21
7
18
43
10
47
36
24
22
40"""

import itertools

numbers = [int(line) for line in string.split("\n")]
numbers_dict = {}
for i, num in enumerate(numbers) :
    
numbers_dict = {i:[(i)] for i, num in enumerate(numbers)}

while True :
    keys = numbers_dict.keys()
    for combo in itertools.combinations(list(keys), 2) :
        res = numbers[combo[0]]+numbers[combo[1]]
        if res in keys :
            numbers_dict[res].append(())
        
    quit()
