# Develop a program that read the name, age and sex of 4 ppl.
# At the end the program, show:

# The average of the ages.
# The name of the oldest man.
# The quantity of women below 20 years old.

counter1 = 0
sum_age = 0
oldestM_age = 0
oldestM_name = ''
women_20 = 0

for ppl4 in range(1, 5):
    print(f'{ppl4} ° person')
    name = str(input('name: ')).strip()
    age = int(input('age: '))
    sex = str(input('sex: [m/f] ')).strip().upper()
    counter1 += 1
    sum_age += age
    if ppl4 == 1 and sex == 'M':
        oldestM_age = age
        oldestM_name = name
    if sex == 'M' and age > oldestM_age:
        oldestM_age = age
        oldestM_name = name
    if sex in 'Ff' and age < 20:
        women_20 += 1
print(f'the average of the ages was {sum_age/counter1:.1f} years')
print(f'the name of the oldest man is {oldestM_name} and he has {oldestM_age} years old.')
print(f'the quantity of women under 20 is {women_20}.')
