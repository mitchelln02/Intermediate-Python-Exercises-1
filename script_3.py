result = {}

string = input('Input a string: ')
string = string.lower()
for letter in string:
    if letter not in result:
        result[letter] = 1
    else:
        result[letter] += 1
    
print (result)