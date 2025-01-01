# Write a program that makes the computer "think" in an int number among 0 and 5 and,
# ask the user to try to discover which number was chosen by the computer.

# The program must write at the screen whether the user won or lose.

from random import randint
from time import sleep
syst = randint (0,5) # o variável ou nesse caso objeto pode receber uma função, 
# determinada por parenteses aqui neste caso, entre 0 e 5. . [Faz o computador "pensar".]
print('=+=' * 20)
print("I'm gonna think in a number among 0 and 5. Try to guess. .")
print('=+=' *20)
player = int(input('Which number did I think of? ')) # jogador tenta adivinhar. .
print('Processing. .')
sleep (2)
if player == syst:
    print(f"Congratulations, you've won. I thought of number {syst}")
else: 
    print(f"Not this time. Try again. I thought of number {syst}")
