numbers = """
145
3
157
75
84
141
40
20
60
48
15
4
2
21
129
113
54
28
69
42
34
1
155
63
151
8
139
135
33
81
70
132
150
112
102
59
154
53
144
149
116
13
41
156
85
22
165
51
14
125
52
64
16
134
110
71
107
124
164
160
10
25
66
74
161
111
122
166
140
87
126
123
146
35
91
106
133
26
77
19
86
105
39
99
76
58
31
96
78
88
168
119
27
45
9
92
138
38
97
32
7
98
167
95
55
65
"""

import itertools

numbers = sorted([int(number) for number in numbers.split('\n')[1:][:-1]])
numbers = [0]+numbers+[numbers[-1]+3]

def part_one(numbers) :
    difference_one, difference_three = 0, 0
    for i, number in enumerate(numbers[:-1]) :
        if numbers[i+1]-number == 1 :
            difference_one += 1
        elif numbers[i+1]-number == 3 :
            difference_three += 1
    return difference_one*difference_three

def validate(test) :
    for ind in range(len(test)-1) :
        if test[ind+1]-test[ind] > 3 :
            return False
    return True

def get_possible(x) :
    if x == 1 :
        return 2
    elif x == 2 :
        return 4
    inner = 0
    outer = x+1
    array = list(range(1, x+1))
    count = 1
    for length in range(len(array)) :
        for combo in itertools.combinations(array, length) :
            if validate([inner]+list(combo)+[outer]) :
                count += 1
    return count

def prod(array) :
    result = 1
    for x in array :
        result = result*x
    return result

def part_two(numbers) :
    #Remove links of 3
    numbers_split_up = []
    current_addition = []
    continue_next = False
    for i, number in enumerate(numbers) :
        if continue_next :
            try :
                if numbers[i+1]-number == 1 :
                    continue_next = False
                else :
                    print(number)
            except :
                break
            continue
        if numbers[i+1]-number == 3 :
            if current_addition != [] :
                numbers_split_up.append(current_addition)
                current_addition = []
            continue_next = True
        elif numbers[i+1]-number == 1 :
            if number != 0 :
                current_addition.append(number)
    multipliers = []
    multiplier_dict = {}
    for array in numbers_split_up :
        length_of_array = len(array)
        string_length = str(length_of_array)
        try :
            multipliers.append(multiplier_dict[string_length])
        except :
            multiplier_dict[string_length] = get_possible(length_of_array)
            multipliers.append(multiplier_dict[string_length])
    return prod(multipliers)

"""
1, 2, 3, 4
1, 2, 3
1, 2, 4

"""

#print(get_possible([1, 2, 3, 4]))
#quit()
print(numbers)
print(part_two(numbers))
#print(get_possible(3))
    
