# Make a program that helps a MEGA SENA gambler to creat guesses. . 
# The program will ask how many games will be gambled and will sort 6 numbers among 1 and 60 to each game, indexing everything in a compund list.

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-='*30)
print('                       Megasena')
print('-='*30)
quant = int(input('How many games would you like me to sort? '))
tot = 1
cont = 0
while tot <= quant:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont+=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('-=' *3, f'Sorting {quant} Games', '-=' *3)
for i, l in enumerate(jogos):
    print(f'Game {i+1}: {l} ')
    sleep(1)
print('-='*5, '<Good Luck! >', '-='*5)
