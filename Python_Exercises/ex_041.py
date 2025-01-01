# The National Swimming Confederation need a program that read the date of birth of an athlete and show,
# their category, according with the age:

# up to 9: mirim
# up to 14: infant
# up to 19: jr
# up to 25: sênior
# up above: master

from datetime import date
from time import sleep
current = date.today().year
birth = int(input('When were you born? '))
age =  current-birth
print('OK, analysing your age your rank is: ')
sleep(2)
if age <=9:
    print('mirim')
elif age >9 and age <=14: # maior q 9 aqui se faz desnecessário. 
    print('infant')
elif age >14 and age <=19: # maior q 14 desnecessário tb.
    print('jr')
elif age >19 and age <=25: # maior q 19 desnecessário.
    print('sênior')
elif age >25: # dava para fazer apenas com o else tb. .
    print('master')
print(f'Because you are {age} years old.')
