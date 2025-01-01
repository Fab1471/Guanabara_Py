# Create a program that make the computer plays Jokenpô with you. .

from random import randint
from time import sleep

computer = randint(0,2)

print('''Your options: 
[0] Rock
[1] Paper
[2] Scissors''')

player = int(input('What is your move? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('!')
sleep(1)

print('-=-'*20)

if computer == 0:
    computer = str('Rock')
elif computer == 1:
    computer = str('Paper')
elif computer == 2:
    computer = str('Scissors')

if player == 0:
    player = str('Rock')
elif player == 1:
    player = str('Paper')
elif player == 2: 
    player = str('Scissors')

print(f'Computer move: {computer}')
print(f'Your move: {player}')
print('-=-'*20)

if computer == player:
    print('Equal Results, Tie')
elif computer == 'Rock' and player == 'Paper':
    print('Player Wins')
elif computer == 'Rock' and player == 'Scissors':
    print('Computer Wins')
elif computer == 'Paper' and player == 'Rock':
    print('Computer Wins')
elif computer == 'Paper' and player == 'Scissors':
    print('Player Wins')
elif computer == 'Scissors' and player == 'Rock':
    print('Player Wins')
elif computer == 'Scissors' and player == 'Paper':
    print('Computer Wins')
else: 
    print('movement not allowed')


'''

from random import randint
items = ('Rock', 'Paper',  'Scissors')
computer = randint(0,2)
print(f"The computer have chosen {(items[computer])}")

print(f'Computer move: {items[computer]}')

'''
