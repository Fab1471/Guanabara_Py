# Make a program which reads the full name of a person and show in the sequence: 
# The first and the last name separetely. 

# Ex:
# 1st = Ana
# last: Souza

name = str(input('Tell me your name: ')).strip()
divided = name.split()
print(f'Nice to meet you, {name}')
print(f'Your first name is: {divided[0]}')
print(f'Your last name is: {divided[len(divided)-1]}') # -1 dentro dos colchets [] e td dentro das chavs {}
