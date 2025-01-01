# Make a program that reads 3 numbers and show the which one is the highest and which one is the lowest.

a = int(input('1st value: '))
b = int(input('2nd value: '))
c = int(input('3rd value1 '))

# verificando o menor. .
minor =  a
if b<a and b<c:
    minor = b
if c<a and c<b:
    minor = c

print(f'the lowest typed value was: {minor}')

# verificando o maior
major = a
if b>a and b>c:
    major = b
if c>a and c> b:
    major = c

print(f'the highest typed value was: {major}')
