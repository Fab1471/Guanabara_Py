from curses.ascii import isspace


print("Make a program which read something through the keyboard and show at the screen it's primitive type and all the possible pieces of information about it.")


info = (input('type sth:'))
print(f'the primitive type of this value is', (type(info)))
print('are there just spaces?', {info.isspace()})
print(f'is alphabetical?', {info.isalpha()})
print(f'is alphanumeric', {info.isalnum()})
print(f'is it in uppercase?', {info.isupper()})
print(f'is it in lowercase?', {info.islower()})
print(f'is it capitalized?', {info.istitle()})
