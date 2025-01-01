# Make a program which reads the lenght of the opposite and the adjacent sides of a rectangular triangle, 
# calculate and shows the lenght of the Hypotenuse.

'''base = adjacent 'while' perpendicular = opposite'''

# o quadrado da hipotenusa é igual a soma dos quadrados dos catetos. .
# a hipotenusa é a raiz quadrada da soma dos quadrados dos catetos. .

os = float(input('lenght of the opposite side: '))
ad = float(input('lenght of the adjacent side: '))
hy = (os ** 2 + ad ** 2) ** (1/2)
print(f'the hypotenuse will be: {hy}')

from math import hypot
os = float(input('lenght of the opposite side: '))
ad = float(input('lenght of the adjacent side: '))
hyp = hypot(os, ad)
print(f'the hypotenuse will be: {hy}')

# desta segunda maneira apenas importa-se a função hypot 
# aplicamos a hypot em uma variável e damos os 2 indicadores necessários para o cálculo
# o cateto oposto e o cateto adjacente. .
