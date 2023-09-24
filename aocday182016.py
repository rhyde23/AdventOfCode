#AOC Day 18 2016
string = ".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^...."
#string = ".^^.^.^^^^"
import time
def getNextChar(t) :
    if t in ["^^.", ".^^", "^..", "..^"] :
        return "^"
    return "."

def getNextRow(last_row) :
    return getNextChar("."+last_row[:2])+"".join([getNextChar(last_row[last_ind-2:last_ind+1]) for last_ind in range(2, len(last_row), 1)])+getNextChar(last_row[-2:]+".")

def main(s) :
    total = s.count(".")
    #print(total)
    for x in range(399999) :
        s = getNextRow(s)
        #print(s.count("."))
        total += s.count(".")
    return total
start = time.time()
print(main(string), time.time()-start)
