from stat import FILE_ATTRIBUTE_INTEGRITY_STREAM
from unicodedata import name


cont = 1
while cont <= 10:
    print(cont, '->', end=' ') # colocar vírgula aspas cm -> mais vírgula e o end igual aspas e espaço, espaça os termos em linha reta e dps puxa o end para o lado também. .
    cont+=1 # faz com q cont receba ele e mais 1. .
print('end')

n = cont = 0
while cont<5:
    n = int(input('type a number: '))
    cont+=1

n = 0
while n != 999: # reoetição com enquanto usando 'flags' [cabô, cabô, cabô. .]
    n = int(input('type a number: '))

n = s = 0 # no python não declaramos variáveis, apenas inicializamos. .
while n != 999:
    n = int(input('type a number: '))
    s +=n
s -= 999 # gambiarra para remover os 999 da flag. .
print(f'The sum is {s}') # aqui ele vai somar também o ponto de parada, a flag. .

n = s = 0
while True:
    n = int(input('type a number: '))
    if n == 999:
        break
    s+=n
print(f'The sum is {s}')

# f strings

name = 'Fabri'
age = 27
print(f'{name} has {age} years.') # Python 3 Enhanced
print('{} has {} years.'.format(name, age)) # Python 3
print('%s has %d years.' % (name, age)) # Python 2

# :^20 centraliza em 20 espaços dentro da f string. .
# :-^20 complementa com tracinho ou :->20 alinha direita ou -<20 alinha esquerda. .
