# Create a program that will read several numbers and put them in a list.

# After that show: 

# A: How many numbers were typed.
# B: The list of values ordered in decrescent form.
# c: If the value 5 was or not typed and is or not at the list.

values = []
while True:
    values.append(int(input('type a value: ')))
    answer = str(input('wanna proceed? [y/n] '))
    if answer in "Nn":
        break
print('-='*30)
print(f'you typed {len(values)} elements')
values.sort(reverse=True)
print(f'the values in reverse order are {values}')
if 5 in values:
    print('the value 5 is part of the list')
else:
    print('the value 5 is not in the list')
