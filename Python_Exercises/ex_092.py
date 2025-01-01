# Create a program that reads, name and year of birth and work card of a person and
# index them (with age) in a dictionary. If by any chance the word card was different from zero, the dictionary will receive also the hiring year and the salary.
# Calculate and add, besides the age, with how many years the person is going to retire.

from datetime import datetime
data = dict()
data['name'] = str(input('Name: '))
birth = int(input('Birth Year: '))
data['age'] = datetime.now().year - birth
data['ctps'] = int(input('Work Register (0 means negative): '))
if data['ctps'] != 0:
    data['hiring'] = int(input(' Hiring Year: '))
    data['salary'] = float(input('Salary: '))
    data['retirement'] = data['age'] + (data['hiring'] + 35) - datetime.now().year
print('-='*30)
for k, v in data.items():
    print(f'  -{k} has the value {v} ')
