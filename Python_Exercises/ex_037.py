# Write a program that reads an int number and ask the user to choose which will be the conversion base:
# 1 to binary
# 2 to octal
# 3 to hexadecimal
# Bases Numéricas

num = int(input('type an int number: '))
print('''Choose one of the bases to the conversion: 
[1] convert to Binary
[2] convert to Octal
[3] convert to Hexadecimal''')
option = int(input('Your option: '))
if option == 1:
    print(f'{num} converted to binary equals {bin(num)[2:]}')
elif option == 2:
    print(f'{num} converted to Octal equals {oct(num)[2:]}')
elif option == 3:
    print(f'{num} converted to Hexadecimal equals {hex(num)[2:]}')
else: 
    print('Invalid option. Please, try again.')
