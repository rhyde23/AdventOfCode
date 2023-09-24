#AOC Day 12 2016

string = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 13 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""

variables = {"a":0, "b":0, "c":1}

def get_value(s) :
    if s in variables :
        return variables[s]
    else :
        return int(s)

def main() :
    lines = string.split("\n")
    i = 0
    while i < len(lines) :
        line = lines[i]
        spaced = line.split(" ")
        if spaced[0] == "cpy" :
            variables[spaced[2]] = get_value(spaced[1])
        elif spaced[0] == "inc" :
            variables[spaced[1]] += 1
        elif spaced[0] == "dec" :
            variables[spaced[1]] -= 1
        elif spaced[0] == "jnz" :
            if get_value(spaced[1]) != 0 :
                i += int(spaced[2])-1
        i += 1
    return variables['a']

print(main())
