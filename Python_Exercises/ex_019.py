# A professor wants to draw one of his 4 students to erase the board.
# Make a program that helps him. Reading the name of all the 4 students and 
# writing the name of the chosen one.

from random import choice
n1 = str(input('1st name: '))
n2 = str(input('2nd name: '))
n3 = str(input('3rd name: '))
n4 = str(input('4th name: '))
list = [n1, n2, n3, n4]
chosen = choice(list) #variável recebe *random.choice(de outra variável aqui dentro dos parenteses)*
print(f'The chosen student was: {chosen}')
