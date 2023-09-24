#AOC Day 16 2015

key_string = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
import re

def find_amts(s) :
    amts = {}
    for finding in re.findall("[a-z]+\:\s[0-9]+", s) :
        splitted = finding.split(": ")
        amts[splitted[0]] = int(splitted[1])
    return amts

key_amounts = find_amts(key_string)

def validateLine(line) :
    amounts = find_amts(line)
    for key in amounts :
        if key in ["cats", "trees"]:
            if amounts[key] <= key_amounts[key] :
                return False
        elif key in ["pomeranians", "goldfish"]:
            if amounts[key] >= key_amounts[key] :
                return False
        else :
            if key_amounts[key] != amounts[key] :
                return False
    return True

with open('aocday162015.txt') as f:
    lines = f.readlines()

for i, line in enumerate(lines) :
    if validateLine(line) :
        print(i+1)
