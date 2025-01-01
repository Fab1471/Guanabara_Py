# Make a program that show at the screen a regressive count for the fireworks burst,
# starting from 10 to 0, with a pause of 1 second between them.

from time import sleep
from datetime import date
for contador in range(10, -1, -1):     # aqui se necessita de uma variável de controle
    print(contador)                    # neste caso o 'contador' é nossa variável de controle
    sleep(0.5)                           # o passo é o menos 1
print(f'Happy {date.today().year+1}')
