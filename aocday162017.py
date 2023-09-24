#AOC Day 16 2017

with open('aocday162017.txt') as f:
    lines = f.readlines()[0]

#lines = "s1,x3/4,pe/b"
s = "abcdefghijklmnop"
#s = "abcde"
s = list(s)

def processInstruction(ins) :
    global s
    if ins[0] == 's' :
        value = int(ins[1:])
        s = s[-value:]+s[:-value]
    elif ins[0] == 'x' :
        splitted = ins[1:].split("/")
        index1, index2 = int(splitted[0]), int(splitted[1])
        swap1, swap2 = s[index1], s[index2]
        #print(s, index1, swap2)
        s[index1] = swap2
        s[index2] = swap1
    else :
        splitted = ins[1:].split("/")
        #print(splitted)
        index1, index2 = s.index(splitted[0]), s.index(splitted[1])
        s[index1] = splitted[1]
        s[index2] = splitted[0]

def main() :
    for instruction in lines.split(",") :
        processInstruction(instruction)

billion = 1000000000
found = []
while True :
    main()
    res = ''.join(s)
    if not res in found :
        found.append(res)
    else :
        break

print(found[(billion%len(found))-1])
