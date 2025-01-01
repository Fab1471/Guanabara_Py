# Remake the challenge 51, reading the 1st term and the reason of a arithmetic progression,
# showing the 10 first numbers, using the structure while.

print('Arithmetic Progression Generator')
print('-='*10)
first = int(input('1st number: '))
reason = int(input('reason: '))
term = first
count = 1
while count <= 10:
    print(f'{term} --> ', end=' ')
    term+=reason
    count+=1
print('end')
