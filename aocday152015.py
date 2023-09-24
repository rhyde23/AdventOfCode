
#Could solve this using some multivariable calc
#AOC Day 15 2015

import re
import numpy as np

string = """Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8"""


#string = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
#Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

def initialize() :
    splitted_by_line = string.split("\n")
    num_of_ingredients = len(splitted_by_line)
    amounts = [int(100/num_of_ingredients) for i in range(num_of_ingredients)]
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
    last = -1
    last_array = []
    last_amts = []
    while True :
        global big
        currentProdTotal = np.prod(big)
        potential_changes = calculatePotentialChanges(currentProdTotal)
        min_ind, max_ind = potential_changes.index(min(potential_changes)), potential_changes.index(max(potential_changes))
        amounts[min_ind] -= 1
        amounts[max_ind] += 1
        big = np.add(big, np.add(factors[max_ind], factors[min_ind]*-1))
        if last < currentProdTotal :
            last = currentProdTotal
            last_array = big
            last_amts = amounts
        else :
            print("Final: ", last_amts, last)
            break
        print(amounts, currentProdTotal, sum(np.multiply(amounts, calories)))
        
main()
