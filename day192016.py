#AOC Day 19 2016

def updateFLS(first, last, skip) :
    amt = ((last-first)/skip)+1
    if amt % 2 == 0 :
        return first, last-skip, skip*2
    else :
        return first+(skip*2), last, skip*2

def main(first, last, skip) :
    while True :
        first, last, skip = updateFLS(first, last, skip)
        if first == last :
            return first

print(main(1, 3001330, 1))
