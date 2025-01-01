# Make a program that play even or odd with the computer.
# The game will just stop when the player loses,
# showing the total of consecutive victories that they 
# conquered at the end of the game.

from random import randint
victory = 0
while True:
    print('-'*30)
    print("Let's play even or odd!")
    player = int(input('type a value: '))
    computer = randint(0, 10)
    total = player + computer
    print('-'*30)
    type = ' '
    while type not in 'EeOo':
        type = str(input('even or odd? [e/o] ')).strip().lower()[0]
    print(f'you played {player} and the computer played {computer}. Total of {total} ', end=' ')
    print('EVEN' if total % 2 == 0 else 'ODD')
    if type == 'e':
        if total % 2 == 0:
            print('You won!')
            victory+=1
        else:
            print('You lose.')
            break
    elif type == 'o':
        if total % 2 == 1:
            print('You won!')
            victory+=1
        else:
            print('You lose.')
            break
    print("let's play again!")
print(f"game over! you've won {victory} times")
