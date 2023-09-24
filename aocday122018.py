#AOC Day 12 2018

state = "##.######...#.##.#...#...##.####..###.#.##.#.##...##..#...##.#..##....##...........#.#.#..###.#"

instructions = """.###. => #
#.##. => .
.#.## => #
...## => .
###.# => #
##.## => .
..... => .
#..#. => #
..#.. => #
#.### => #
##.#. => .
..#.# => #
#.#.# => #
.##.# => #
.#..# => #
#..## => #
##..# => #
#...# => .
...#. => #
##### => .
###.. => #
#.#.. => .
....# => .
.#### => #
..### => .
..##. => #
.##.. => .
#.... => .
####. => #
.#.#. => .
.#... => #
##... => #"""


instructions_dict = {ins[:5]:ins[-1] for ins in instructions.split("\n")}

print(instructions)
print()

def main() :
    global state
    leftmost_index = 0
    print(state, leftmost_index)
    for cycles in range(20) :
        new_state = ""
        add_front = 5-state.index("#")
        if add_front > 0 :
            state = "."*add_front+state
            leftmost_index -= add_front
        leftmost_index += 2
        add_back = 5-state[::-1].index("#")
        if add_back > 0 :
            state = state+"."*add_back
        #print("before sliding", state)
        for sliding_window in range(0, len(state)-4, 1) :
            new_state = new_state + instructions_dict[state[sliding_window:sliding_window+5]]
        state = new_state
        ind = state.index("#")
        if ind != 0 :
            state = state[ind:]
            leftmost_index += ind
        ind = state[::-1].index("#")
        if ind != 0 :
            state = state[:-(ind)]
        print(state, leftmost_index)
    total = 0
    for i in range(len(state)) :
        if state[i] == "#" :
            total += (i+leftmost_index)
    print(state)
    return total


print(main())
        
