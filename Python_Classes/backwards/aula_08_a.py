import math
num = int(input(' type a number: '))
sqr = math.sqrt(num)
print(f'The square root of {num} equals {math.ceil(sqr)}')
print(f'The square root of {num} equals {math.floor(sqr)}')
print(f'The square root of {num} equals {sqr:.2f}')
#math.ceil(variável) td isso dentro das chaves do format. . arredonda pra cima, floor pra baixo. .
#:.2float faz com q seja 2 casas de float, decimais. .

from math import sqrt, floor # é possível utilizar assim tb. .
num = int(input(' type a number: '))
sqr = sqrt(num)
print(f'The square root of {num} equals {sqr:.2f}')
print(f'The square root of {num} equals {floor(sqr)}') #se for colocar aux tem q colocar a variável 
#entre parenteses. .
