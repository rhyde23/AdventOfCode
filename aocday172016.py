#AOC Day 17 2016

Part One
import hashlib

puzzle_input = "awrkjxxr"
#puzzle_input = "ulqzkmiv"   


def convertStringToHex(s) :
    return hashlib.md5(puzzle_input.encode()).hexdigest()

def getCurrentPos(s) :
    return (s.count("R")-s.count("L"), s.count("D")-s.count("U"))

def canGo(cp) :
    return [cp[1] > 0, cp[1] < 3, cp[0] > 0, cp[0] < 3]

def get_neighbors(hex_string, cp) :
    possibilities = ["U", "D", "L", "R"]
    cGs = canGo(cp)
    return [puzzle_input+possibilities[i] for i in range(4) if hex_string[i] in ['b', 'c', 'd', 'e', 'f'] and cGs[i]]

def bfs(starting_node) :
    queue = []
    queue.append(starting_node) 
    while True :
        s = queue.pop(0)
        global puzzle_input
        puzzle_input = s
        current_pos = getCurrentPos(puzzle_input)
        if current_pos == (3, 3) :
            return s
        for p in get_neighbors(convertStringToHex(s), current_pos):
            queue.append(p)

print(bfs(puzzle_input))

"""
#Part 2 
import hashlib, re

puzzle_input = "awrkjxxr"
puzzle_input = "ihgpwlah"


def convertStringToHex(s) :
    return hashlib.md5(puzzle_input.encode()).hexdigest()

def getCurrentPos(s) :
    return (s.count("R")-s.count("L"), s.count("D")-s.count("U"))

def canGo(cp) :
    return [cp[1] > 0, cp[1] < 3, cp[0] > 0, cp[0] < 3]

def get_neighbors(hex_string, cp) :
    possibilities = ["U", "D", "L", "R"]
    cGs = canGo(cp)
    return [puzzle_input+possibilities[i] for i in range(4) if hex_string[i] in ['b', 'c', 'd', 'e', 'f'] and cGs[i]]

def bfs(starting_node) :
    queue = []
    queue.append(starting_node)
    maximum = 0
    while queue != [] :
        s = queue.pop(0)
        global puzzle_input
        puzzle_input = s
        current_pos = getCurrentPos(puzzle_input)
        if current_pos == (3, 3) :
            maximum = max(maximum, len(re.findall("[A-Z]", puzzle_input)))
        for p in get_neighbors(convertStringToHex(s), current_pos):
            queue.append(p)
    return maximum

print(bfs(puzzle_input))
"""

