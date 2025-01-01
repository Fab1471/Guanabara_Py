# Improve the game from de challenge 028 where the computer thinks in a number among 0 and 10.
# But, now the player will try to guess untill the guess ir correct, 
# showing at the end how many guesses where
# necessary for them to win. .

from random import randint
syst = randint (0, 10)
i = 0
print('I am you computer. .')
print('just thought of a number among 0 and 10. .')
print('are you able to guess which number I though of? ')
guess = int(input('what is your guess? '))
while guess != syst:
    i+=1
    if guess < syst:
        print('more. .')
    else:
        print('less. .')
    guess = int(input('wrong guess. try again: '))
print(f'congratulations, that was the number I thought of! I thought of number {syst}!')
print(f'and you had to use {i+1} guesses to guess the corret answer.')


'''Guanabara Version

from random import randint
computador = randint (0, 10)
print('Sou seu computador. . Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites =+1
    if jogador == computador:
        acertou = True
    else: 
        if jogador < computador:
            print('mais. . tente mais uma vez. .')
        elif jogardor > computador:
            print('menos. . tente mais uma vez. .')
print(f'Acertou com {palpites} tentativas. Parabéns!')'''
