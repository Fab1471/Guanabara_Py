# Make a program where 4 players play a dice and got random results.
# Save those results in a dictionary. At the end, put that dictionary in order, considering that the winner got the biggest number in the dice.

from random import randint
from time import sleep
from operator import itemgetter
game = {'player 1': randint(1, 6),
        'player 2': randint(1, 6),
        'player 3': randint(1, 6),
        'player 4': randint(1, 6)}
ranking = list()
print('Sorted Values:')
for k, v in game.items():
    print(f'{k} got {v} from the dice roll')
    sleep(1)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('== Results ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º place: {v[0]} with {v[1]}')
    sleep(1)
