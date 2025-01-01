# Improve the challenge 061, asking the user if they wanna show some more terms.
# The program ends when they say they wanna show 0 terms.

print('Arithmetic Progression Generator')
print('-='*10)
first = int(input('1st number: '))
reason = int(input('reason: '))
term = first
count = 1
total = 0
more = 10
while more != 0:
    total+=more
    while count <= total:
        print(f'{term} --> ', end=' ')
        term+=reason
        count+=1
    print('pause')
    more = int(input('How many more terms do you wanna show? '))
print(f'progression ended with {total} terms')
