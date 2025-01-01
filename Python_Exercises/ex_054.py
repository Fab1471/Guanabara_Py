# Make a program that read the birth year of 7 ppl.
# At the end, show how many ppl did not reach 21 years.
# and how many already reached 21 years.

from datetime import date
current = date.today().year
tadult = 0
tnoage = 0
for person in range(1, 8):
    birth = int(input(f"what is the {person}º person's birth year? "))
    age = current - birth
    print(age)
    if age >=21:
        tadult+=1
        print('21 complete, adulthood')
    else:
        tnoage+=1
        print('21 not complete yet, nonage')
print(f'we have a total of {tadult} persons that already reached adulthood')
print(f'we have a total of {tnoage} persons that have not reached adulthood yet')
