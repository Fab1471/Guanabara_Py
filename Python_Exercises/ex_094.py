# Create a program that reads name, sex and age of several ppl, saving the data of each person in a dictionary and all dictionaries in a list.
# At the end, show:
# A: How many ppl were indexed.
# B: The average of age of the group.
# C: A list with all the women.
# D: A list with all the ppl with age over the average.

ppl = list()
person = dict()
plus = average = 0
while True:
    person.clear()
    person['name'] = str(input('Nome: '))
    while True:
        person['sex'] = str(input('Sex: [M/F] ')).upper()[0]
        if person['sex'] in 'MF':
            break
        print('ERROR! Please, type just M or F. ')
    person['age'] = int(input('Age: '))
    plus += person['age']
    ppl.append(person.copy()) # copy of the info
    while True:
        answer = str(input('Wanna continue? [Y/N] ' )).upper()[0]
        if answer in 'YN':
            break
        print('ERROR! Answer only Y or N! ')
    if answer == 'N':
        break
print('-='*30)

# Analysis above, execution below.

print(f'A) In total we have {len(ppl)} ppl registred. ')
average = plus / len(ppl)
print(f'B) The average age is {average:5.2f} years. ')
print('C) The registered women were ', end=' ')
for p in ppl:
    if p['sex'] in 'Ff':
        print(f'{p["name"]} ', end=' ')
print()
print('D) List of ppl that are above the average: ', end=' ')
for p in ppl:
    if p['age'] >= average:
        print('      ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v} ', end=' ')
            print()
print('<< Finished >>')
