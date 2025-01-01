# Create a program that reads name and weight of several ppl, saving all in a list. At the end show:

# A: How many ppl were indexed.
# B: A list with the heaviest ppl.
# C: A list with the lightest ppl.

temp = []
mainlist = []
mai = men = 0
while True:
    temp.append(str(input('Name: ')))
    temp.append(float(input('Weight: ')))
    if len(mainlist) == 0:
         mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    mainlist.append(temp[:])
    temp.clear()
    answer = str(input('Wanna continue? [y/n] '))
    if answer in 'Nn':
        break
print('-='*30)
print(f'The data were {mainlist}')
print(f'You indexed a total of {len(mainlist)} ppl. .')
print(f'the highest weight was of {mai} kilograms. ' 'Weight of ', end='')
for p in mainlist:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
    print()
print(f'the lowest weight was of {men} kilograms. ' 'Weight of', end='')
for p in mainlist:
    if p[1] ==men:
        print(f'[{p[0]}]')
print()
