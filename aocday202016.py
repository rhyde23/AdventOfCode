#AOC Day 20 2016

with open('day202016.txt') as f:
    lines = f.readlines()

#lines = ["6-7",
#"0-2",
#"4-7",
#         ]

blacklisted = []

def action(left, right, middle, start, end) :
    global blacklisted
    c = False
    middle_range = blacklisted[middle]
    if end < middle_range[0] :
        right = middle
    elif start > middle_range[1] :
        left = middle
    else :
        c = True
        if end >= middle_range[0] and start < middle_range[0] :
            blacklisted[middle][0] = start
        if end >= middle_range[1] and start < middle_range[1] :
            blacklisted[middle][1] = end
        if middle != 0 :
            if blacklisted[middle-1][1] > blacklisted[middle][0] :
                blacklisted[middle][0] = blacklisted[middle-1][0]
                del blacklisted[middle-1]
        if middle != len(blacklisted)-1 :
            if blacklisted[middle+1][0] < blacklisted[middle][1] :
                blacklisted[middle][1] = blacklisted[middle+1][1]
                del blacklisted[middle+1]
    return left, right, c

def binary_search(start, end) :
    global blacklisted
    left, right = 0, len(blacklisted)-1
    if blacklisted == [] :
        blacklisted.append([start, end])
        return None
    last_middle = -1
    last_one = False
    while True :
        middle = (left+right)//2
        if middle == last_middle :
            if left < right :
                middle += 1
                left, right, c = action(left, right, middle, start, end)
            #else :
                #print(left, right, middle, blacklisted[0], [start, end])
            if not c :
                #print()
                #if middle == len(blacklisted)-1 :
                    #blacklisted.append([start, end])
                #else :
                    #blacklisted.insert(middle, [start, end])
                blacklisted.append([start, end])
                blacklisted = list(sorted(blacklisted))
            break
        left, right, c = action(left, right, middle, start, end)
        if c :
            break
        last_middle = middle
    

def main() :
    for line in lines :
        s, e = line.split("-")
        binary_search(int(s), int(e))
    print(blacklisted==sorted(blacklisted, key=lambda x:x[0]))
    print(sorted(blacklisted, key=lambda x:x[0]))
    #print(36411396-1)
        

main()
