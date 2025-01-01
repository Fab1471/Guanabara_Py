# Make a program that read the birth year of a young man and inform accordingly with his age:

# He will still enlist in the military
# If it's time for him to enlist.
# If it's past enlistment time already.

# Your program also need to show the time untill or past the due date to enlist.

from datetime import date
current = date.today().year # formula para pegar a data de hoje de acordo com calendário config. .
birth = int(input('birth year: '))
age = current - birth
print(f'Who was born in {birth} has {age} years in {current}')
if age == 18:
    print('You must enlist immediately!')
elif age < 18:
    saldo = 18 - age # 18 menos a idade do jovem, vai dizer qts anos faltam, saldo. .
    print(f'You do no have 18 years yet. Still {saldo} years to go.')
    year = current+saldo # ano atual mais saldo, dirá em q ano será o alistamento. .
    print(f'Your enlistment will be in {year}')
elif age > 18:
    saldo = age - 18 # idade menos 18 anos vai dar o saldo de anos. .
    print(f'You should have already enlisted {saldo} years ago!')
    year = current-saldo # ano atual menos o saldo de anos vai dar o ano que tinha q ter alistado. .
    print(f'Your elistment was in {year}')
