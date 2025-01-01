# Make a program that read an int number and show it's factorial. 
  
# 5! =  5x4x3x2x1 = 120

# dps dá para tentar fazer com for tb. .

n = int(input('type a number to calculate the factorial: '))
c = n
f = 1 # multiplicação limpa começa com 1 e soma com 0
print(f'Calculating {n}! = ', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f*=c # fatorial mais fatorial vezes o c
    c-=1
print(f'{f}')
