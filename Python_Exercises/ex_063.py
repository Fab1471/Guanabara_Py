# Write a program that read a any 'n' int number and show at the screen the 'n' first elements of 
# a fibonacci sequence.

# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print('-'*20)
print('Fibonacci Sequence')
print('-'*20)
n = int(input('how many terms do you wanna show? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2}', end=' ')
count = 3
while count <= n:
    t3 = t1+t2
    print(f'-> {t3}', end=' ')
    t1 = t2
    t2 = t3
    count+=1
print('-> end. .')
print('~'*30)
