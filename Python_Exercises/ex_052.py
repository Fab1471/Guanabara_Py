# Make a program that read an in number and tell if it is or not a prime number.
# a prime number is divisible only by itself or 1. .

num = int(input('type a number: '))
total = 0
for c in range(1, num+1):
    if num%c==0:
        print('\033[34m', end=' ') # blue if divisible
        total+=1
    else:
        print('\033[31m', end=' ') # red if not divisible
    print(f'{c} ', end=' ')
print(f'\n\033[mThe number {num} was divisible {total} times.')
if total ==2:
    print('prime number')
else:
    print('not a prime number')
