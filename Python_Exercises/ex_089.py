# Create a program that reads name and 2 grades of several students and save everthing in a compound list.
# At the end, show a report card with the average of each one and allow the user to find the grades of each student separately.

token = list()
while True:
    name = str(input('Name: '))
    n1 = float(input('1st score: '))
    n2 = float(input('2nd score: '))
    average = (n1+n2) / 2
    token.append([name, [n1, n2], average])
    answer = str(input(' Wanna continue? [y/n] '))
    if answer in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"Name":<10}{"Average":>8}')
print('-'*26)
for i, a in enumerate(token):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('What student do you wanna check the grades? (999 interrupts) '))
    if opc == 999:
        print('Ending. .')
        break
    if opc <= len(token) - 1:
        print(f'Grades of {token[opc][0]} are {token[opc][1]}')
print('<<< You are welcome! >>>')
