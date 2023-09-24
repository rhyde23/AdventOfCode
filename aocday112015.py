import string
lowercase = string.ascii_lowercase

def getNextPassword(password_list) :
    count = -1
    while True :
        if password_list[count] == 25 :
            password_list[count] = 0
            count -= 1
        else :
            password_list[count] += 1
            if password_list[count] in [8, 14, 11] :
                password_list[count] += 1
            return password_list

def verifyPassword(p_list) :
    double_count = 0
    only_double = None
    straight = False
    current_straights = 1
    last = p_list[0]
    for value in p_list[1:] :
        if value == last+1 :
            current_straights += 1
        else :
            if current_straights >= 3 :
                straight = True
            current_straights = 1
            if value == last and value != only_double :
                double_count += 1
                only_double = value
        last = value
    if straight and double_count >= 2 :
        return True
    return False

def main(p) :
    password_list = [lowercase.index(c) for c in p]
    while True :
        password_list = getNextPassword(password_list)
        if verifyPassword(password_list) :
            return ''.join([lowercase[ind] for ind in password_list])
    

p = 'cqjxxyzz'
print(main(p))
