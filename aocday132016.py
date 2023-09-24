#AOC Day 13 2016

puzzle_input = 1350
end_node = (31, 39)
#puzzle_input = 10
#end_node = (7, 4)
known_states = {}

visited = []
within_fifty = {(1, 1):0}


def get_state(coord) :
    x, y = coord
    return bin((x*x)+(3*x)+(2*x*y)+y+(y*y)+puzzle_input)[2:].count("1") % 2 == 0

def is_open(coord) :
    if coord in visited :
        return False
    if coord in known_states :
        return known_states[coord]
    state = get_state(coord)
    known_states[coord] = state
    return state

def get_neighbors(coord) :
    return filter(is_open, [(coord[0]+1, coord[1]), (coord[0]-1, coord[1]), (coord[0], coord[1]+1), (coord[0], coord[1]-1)])


def dfs(at) :
    if not at in visited :
        visited.append(at)
        #print(within_fifty[at], at)
        for neighbor in get_neighbors(at) :
            if within_fifty[at]+1 <= 50 and neighbor[0] > 0 and neighbor[1] > 0:
                within_fifty[neighbor] = within_fifty[at]+1
                print(neighbor, within_fifty[at]+1)
                dfs(neighbor)
dfs((1, 1))

print(len(within_fifty))

#print(within_fifty)

"""
import sys

sys.setrecursionlimit(50)

visited = []
global within_fifty
within_fifty = 0

def dfs(at) :
    if not at in visited :
        visited.append(at)
        for neighbor in get_neighbors(at) :
            global within_fifty
            within_fifty += 1
            dfs(neighbor)

dfs(end_node)

print(within_fifty)
"""

"""BREADTH FIRST SEARCH FOR PART ONE 
def solve(s) :
    q = [s]
    visited = [s]
    prev = {}
    found = False
    while not found :
        current_node = q[0]
        for neighbor in get_neighbors(current_node) :
            if not neighbor in visited :
                q.append(neighbor)
                visited.append(neighbor)
                prev[neighbor] = current_node
                if neighbor == end_node :
                    found = True
                    break
        q = q[1:]
    return prev
                    
def reconstructPath(s, e, prev) :
    path = []
    at = e
    while True :
        path.append(at)
        if at in prev :
            at = prev[at]
        else :
            break
    path = path[::-1]
    if path[0] == s :
        return path
    return "Path not connected"

def bfs(s, e) :
    prev = solve(s)
    return reconstructPath(s, e, prev)

print(len(bfs((1, 1), end_node))-1)
"""
