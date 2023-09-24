#AOC Day 14 2018 PART 1


def partOne(puzzle_input) :
    #Initialize Recipes string
    recipes = "37"

    #Set both elf indexes
    elf1_index, elf2_index = 0, 1

    #Loop until there are puzzle input + 10 amount of recipe numbers
    while len(recipes) < puzzle_input+10 :

        #Get integer versions of recipe numbers at both elf indexes
        num1, num2 = int(recipes[elf1_index]), int(recipes[elf2_index])

        #Add their sum to the end of the recipes string
        recipes = recipes + str(num1+num2)

        #Update elf indexes and account for exceeding length of string and looping them back to the start of the string with modulus
        elf1_index = (elf1_index+num1+1) % len(recipes)
        elf2_index = (elf2_index+num2+1) % len(recipes)

    #Return string of characters from puzzle input to puzzle input + 10
    return recipes[puzzle_input:puzzle_input+10]

print(partOne(290431))


#AOC Day 14 2018 PART 2

def partTwo(puzzle_input) :
    #Change puzzle input to string
    puzzle_input = str(puzzle_input)

    #Get length of puzzle input
    length = len(puzzle_input)

    #Initialize Recipes string
    recipes = "37"

    #Set both elf indexes
    elf1_index, elf2_index = 0, 1

    #Loop indefinitely, easier to put return statements inside of loop in this case
    while True :
        
        #Get integer versions of recipe numbers at both elf indexes
        num1, num2 = int(recipes[elf1_index]), int(recipes[elf2_index])

        #Add their sum to the end of the recipes string
        recipes = recipes + str(num1+num2)

        #WE EITHER ADD ONE OR TWO CHARACTERS TO THE END OF THE STRING EVERY LOOP, SO WE MUST CHECK THE CONDITION OF THE LAST LENGTH AMOUNT MATCHING
        #THE PUZZLE INPUT BUT ALSO HAVE TO CHECK IF TWO CHARACTERS ARE ADDED AND IF THE FIRST ONE SATISFIES THE PUZZLE INPUT TOO.
        if recipes[-length:] == puzzle_input :
            return len(recipes)-length
        if recipes[-(length+1):-1] == puzzle_input :
            return len(recipes)-(length+1)

        #Update elf indexes and account for exceeding length of string and looping them back to the start of the string with modulus
        elf1_index = (elf1_index+num1+1) % len(recipes)
        elf2_index = (elf2_index+num2+1) % len(recipes)

print(partTwo(290431))
