alphabet = ['a','b','c','d','e']
first_letter = alphabet[0]
last_letter = alphabet[-1]
first_three = alphabet[:3]
last_three = alphabet[-3:]
alphabet.append('f')
alphabet.append('g')
alphabet.append('h')
print(last_three)
last_three = alphabet[-3:]
print(last_three)
alphabet.pop(-1)
print(alphabet)