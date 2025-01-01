# Make a program which reads a number from 0 to 9999 and show  at the screen each one of the digits separately.
# Ex: 
# Digite número: 1834

# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

# tentar como string e tb matematicamente. .

num = int(input('type a number from 0 to 9999: '))
unit = num // 1 % 10
ten = num // 10 % 10
hundred = num // 100 % 10
thousand = num // 1000 % 10
print(f'Analysing the number {num}')
print(f'unit: {unit}')
print(f'ten: {ten}')
print(f'hundred: {hundred}')
print(f'thousand: {thousand}')
