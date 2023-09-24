#Read text file input
with open('aocday122015.txt') as f:
    lines = f.readlines()[0]

#Import Regular Expression library 
import re

#no_goes is a list of indexes of numbers that we won't add
no_goes = []

#function that returns sum of all the numbers in a string as long as they aren't in no_goes
def getSumOfIntegersInString(string) :
    return sum([int(x.group()) for x in re.finditer("\-*[0-9]+", string) if not x.span()[0] in no_goes])

#function that updates the public no_goes list given a section of the string that is bad
def updateNoGoes(section, start) :
    for finding in re.finditer("\-*[0-9]+", section) :
        ind = start+finding.span()[0]
        if not ind in no_goes :
            no_goes.append(ind)

#Main function

def main(lines) :
    open_q = []
    found_reds = []
    for finding in re.finditer("[{}]", lines) :
        s, pos = finding.group(), finding.span()[0]
        if s == "{" :
            open_q.append(pos)
        else :
            section = lines[open_q[-1]:pos+1]
            trig = False
            for instance in re.finditer("\:\"red\"", section) :
                real_pos = open_q[-1]+instance.span()[0]
                if not real_pos in found_reds :
                    found_reds.append(real_pos)
                    trig = True
            if trig :
                updateNoGoes(section, open_q[-1])
            open_q = open_q[:-1]
    return getSumOfIntegersInString(lines)

print(main(lines))


f.close()

testString = "Hello World"

#print(testString[3:7])
