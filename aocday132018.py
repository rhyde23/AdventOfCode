#AOC Day 13 2018 

with open('aocday132018.txt') as f:
    lines = f.readlines()

size = len(lines[0])

import re

#0 = right, 1 = left, 2 = down, 3 = up
directions_characters = [">", "<", "v", "^"]
forward_slash_changes = {3:0, 0:3, 2:1, 1:2}
backward_slash_changes = {1:3, 3:1, 0:2, 2:0}
right_turns = {0:2, 1:3, 2:1, 3:0}
left_turns = {0:3, 1:2, 2:0, 3:1}
#x_pos, y_pos, direction
carts = []

def processCarts() :
    for i, line in enumerate(lines) :
        for finding in re.finditer("[<>^v]", line) :
            pos, g = finding.span()[0], finding.group()
            carts.append([pos, i, directions_characters.index(g), 1])

def main() :
    global carts
    processCarts()
    while True :
        carts = sorted(carts, key=lambda x: (size*x[1])+x[0])
        #print(carts, times)
        positions_found = []
        for cart in carts :
            if cart[:2] in positions_found :
                print("here1")
                return cart[:2]
            if cart[2] == 0 :
                cart[0] += 1
            elif cart[2] == 1 :
                cart[0] -= 1
            elif cart[2] == 2 :
                cart[1] += 1
            else :
                cart[1] -= 1
            char_on = lines[cart[1]][cart[0]]
            if char_on == "/" :
                cart[2] = forward_slash_changes[cart[2]]
            elif char_on == "\\" :
                cart[2] = backward_slash_changes[cart[2]]
            elif char_on == "+" :
                mod = cart[3] % 3
                if mod == 1 :
                    cart[2] = left_turns[cart[2]]
                elif mod == 0 :
                    cart[2] = right_turns[cart[2]]
                cart[3] += 1
            if cart[:2] in positions_found :
                print("here2")
                return cart[:2]
            positions_found.append(cart[:2])
        #print(positions_found)
        
print(main())
