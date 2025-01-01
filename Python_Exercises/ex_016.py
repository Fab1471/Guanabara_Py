#Create a program that reads any real number through the keyboard 
#and show at the screen it's int part. .

# Example: type a number: 7.27
# The number 7.27 has 7 as it's int part. .

from math import trunc
n1 = float(input('type a value: '))
print(f"The given value was: {n1}\nIt's int part is equivalent to: {trunc(n1)}")

# math.trunc() -  dentro dos parenteses, colocar a variável do valor desejado. (se usar o import math)
# trunc() -  dentro dos parenteses, mesma coisa. porém já não precisa do [math.]
# insere todos os cmds sempre dentro das chaves. .

'''3 aspas fazem com q o programa todo fique como comentário'''

n1 = float(input('type a value: '))
print(f"The given value was: {n1}\nIt's int part is equivalent to: {int(n1)}")
# no segundo exemplo não foi necessária a importação de módulos. .
