#Day 16 2016

starting_input, desired_length = "01111010110010011", 35651584
#starting_input, desired_length = "10000", 20

flip = {"0":"1", "1":"0"}
def flip_characters(s) :
    return ''.join([flip[c] for c in s])

def get_string_to_desired_length(s) :
    while len(s) < desired_length :
        s = ''.join([s, "0", flip_characters(s[::-1])])
    return s[:desired_length]

def checksum(s) :
    return ''.join([str(int(s[i]==s[i+1])) for i in range(0, len(s), 2)])
 
def main() :
    string = get_string_to_desired_length(starting_input)
    while len(string) % 2 == 0 :
       string = checksum(string)
    return string

print(main())
