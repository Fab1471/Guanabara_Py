# Make a program that reads name and average grade of one student, 
# saving also the final situation in a dictionary. At the end, show the content of the structure at the screen.

aluno = dict()
aluno['nome'] = str(input('Name: '))
aluno['average'] = float(input(f'Average of {aluno["nome"]}: '))
if aluno['average'] >= 7:
    aluno['situation'] = 'Approved'
elif 5 <= aluno['average'] < 7:
    aluno['situation'] = 'Summer Classes On'
else:
    aluno['situation'] = 'Disapproved'
print('='*30)
for k, v in aluno.items():
    print(f'  - {k} is {v}')
