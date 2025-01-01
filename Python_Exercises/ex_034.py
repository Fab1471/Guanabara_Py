# Write a program that ask the salary of an employee and calculate it's increase.
# To salaries above R$1250,00, calculate an increase of 10%
# To the ones below or equal, the increase is 15%

salary = float(input('What is your salary? R$ '))
if salary >1250: 
    new = (salary*10)/100 + salary
else:
    new = (salary*15)/100+ salary
print(f'Those whose salary was R${salary:.2f} now receive R${new:.2f}')
