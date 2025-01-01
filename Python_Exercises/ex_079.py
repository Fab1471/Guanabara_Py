# Create a program in which the user can type several numeric values and insert them in a list.
# In case the number already exists in there, he will not be added.
# At the end, all the only values will be displayed in crescent order.

numbers = list()
while True:
    n = int(input('type a value: '))
    if n not in numbers:
        numbers.append(n)
        print('value successfully added')
    else:
        print('duplicate value. not gonna add.')
    r = str(input('wanna proceed? [y/n] '))
    if r in 'Nn':
        break
print('-='*30)
numbers.sort()
print(f'you typed the values {numbers}')
