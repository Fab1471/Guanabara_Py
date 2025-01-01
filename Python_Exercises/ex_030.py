# Create a program that reads an int number and shows if it's even or odd.

number = int(input('Tell me any number: '))
result = number % 2
if result == 0:
    print(f'The number {number} is even.')
else: 
    print(f'The number {number} is odd.')

# o resto da divisão de qlq número par por 2 é 0
# o resto da divisão de qlq número ímpar por 2 é 1
