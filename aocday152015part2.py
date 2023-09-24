#AOC Day 15 2015 part 2
import re
import numpy as np
import itertools

string = """Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8"""


#string = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
#Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

def initialize() :
    splitted_by_line = string.split("\n")
    num_of_ingredients = len(splitted_by_line)
    #amounts = [int(100/num_of_ingredients) for i in range(num_of_ingredients)]
    amounts = [17, 19, 38, 26]
    factors = []
    calories = []
    for line in splitted_by_line :
        nums = re.findall("\-*[0-9]", line)
        factors.append(np.array([int(n) for n in nums[:-1]]))
        calories.append(int(nums[-1]))
    big = np.array([sum([amt*factors[amt_i][type_index] for amt_i, amt in enumerate(amounts)]) for type_index in range(4)])
    return amounts, factors, big, np.array(calories)

amounts, factors, big, calories = initialize()

print(calories)

def calculatePotentialChanges(currentProdTotal) :
    return [np.prod(np.add(big, factors[i]))-currentProdTotal for i, amt in enumerate(amounts)]

def main() :
    while True :
        global big
        currentProdTotal = np.prod(big)
        potential_changes = calculatePotentialChanges(currentProdTotal)
        cals = sum(np.multiply(amounts, calories))
        if cals == 500 :
            print("Final: ", big, amounts, currentProdTotal)
            break
        best_option_combo, best_option_value = None, None
        for combo in itertools.permutations(list(range(len(potential_changes))), 2) :
            result = -potential_changes[combo[0]]+potential_changes[combo[1]]
            cal_change = -calories[combo[0]]+calories[[combo[1]]]
            if (cals > 500 and cal_change < 0) or (cals < 500 and cal_change > 0) :
                print(cals, cal_change, result)
                if best_option_value != None :
                    if result > best_option_value :
                        best_option_value = result
                        best_option_combo = combo
                else :
                    best_option_value = result
                    best_option_combo = combo
        #min_ind, max_ind = potential_changes.index(min(potential_changes)), potential_changes.index(max(potential_changes))
        amounts[best_option_combo[0]] -= 1
        amounts[best_option_combo[1]] += 1
        #print(min_ind, max_ind, best_option_combo, best_option_value, currentProdTotal)
        #quit()
        big = np.add(big, np.add(factors[best_option_combo[1]], factors[best_option_combo[0]]*-1))
            #print("Final: ", last_amts, last)
            #break
        print(amounts, currentProdTotal, sum(np.multiply(amounts, calories)))
        
main()
