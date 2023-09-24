#AOC Day 14 2015

string = """Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds."""

###SOLUTION FOR PART ONE

"""

dur = 2503

def evaluateOne(speed, stamina, rest_period, duration) :
    one_loop_distance, one_loop_duration = (speed*stamina), stamina+rest_period
    modulus = duration%one_loop_duration
    if modulus > stamina :
        second_part = one_loop_distance
    else :
        second_part = modulus*speed
    return (one_loop_distance*((duration-modulus)/one_loop_duration))+second_part

maximum = 0

for line in string.split("\n") :
    split_by_spaces = line.split(" ")
    distance_traveled = evaluateOne(int(split_by_spaces[3]), int(split_by_spaces[6]), int(split_by_spaces[-2]), 2503)
    if distance_traveled > maximum :
        maximum = distance_traveled

print(maximum)
"""

dur = 2503
reindeer = {}

for line in string.split("\n") :
    split_by_spaces = line.split(" ")
    reindeer[(int(split_by_spaces[3]), int(split_by_spaces[6]), int(split_by_spaces[-2]))] = [0, 0, True, 0] #distance traveled, count, mode(True=going, False=resting), points


#reindeer[(14, 10, 127)] = [0, 0, True, 0]
#reindeer[(16, 11, 162)] = [0, 0, True, 0]

for i in range(dur) :
    maximum_distance, maxdistinds = 0, []
    for key in reindeer :
        reindeer[key][1] += 1
        if reindeer[key][1] == key[1]+1 and reindeer[key][2] :
            reindeer[key][2] = False
            reindeer[key][1] = 1
        elif reindeer[key][1] == key[2]+1 and not reindeer[key][2] :
            reindeer[key][2] = True
            reindeer[key][1] = 1
        if reindeer[key][2] :
            reindeer[key][0] += key[0]
        #END OF SECOND
        if reindeer[key][0] > maximum_distance :
            maximum_distance = reindeer[key][0]
            maxdistind = [key]
        elif reindeer[key][0] == maximum_distance :
            maxdistind.append(key)
    for mdi in maxdistind :
        reindeer[mdi][3] += 1

print(max([reindeer[key][3] for key in reindeer]))
            
