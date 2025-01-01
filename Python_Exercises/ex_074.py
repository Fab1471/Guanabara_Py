# Create a program that will generate 5 random numbers and insert them into a Tuple.
# After that, show the list of generated numbers and also point out which one is
# the lowest and highest value that are in the Tuple.

from random import randint
numbers = (randint(1, 10,), randint(1, 10,), randint(1, 10,),
 randint(1, 10,), randint(1, 10,))
print(f'I randomized the values: ', end=(' '))
for n in numbers:
    print(f'{n}', end=' ')
print(f'\nthe highest randomized value was {max(numbers)}')
print(f'the lowest randomized value was {min(numbers)}')
