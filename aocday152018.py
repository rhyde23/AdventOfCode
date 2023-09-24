#AOC Day 15 2015

import re

def main(s) :
    new = ""
    last = s[0]
    count = 1
    for c in s[1:] :
        if c != last :
            new = new + str(count)+last
            last = c
            count = 1
        else :
            count += 1
    new = new + str(count)+last
    return new

string = "1321131112"
for i in range(40) :
    string = main(string)
    print(i, len(string))

print(len(string))

    


