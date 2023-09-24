#AOC Day 17 2017

current_pos = 0

#print(4%3)
#quit()

def moveCurrentPos(step_value, length) :
    global current_pos
    new_position = current_pos+step_value
    if new_position < length :
        current_pos = new_position+1
    else :
        current_pos = new_position%length+1
    
def main(step_value) :
    global current_pos
    spinlock = [0]
    for inserting_value in range(1, 2018, 1) :
        moveCurrentPos(step_value, len(spinlock))
        spinlock.insert(current_pos, inserting_value)
    return spinlock

spin = main(328)
print(spin[current_pos+1])
        
