# Make a program that read the sex of a person but, 
# only accepts the values 'M' or 'F'. 
# if the typed values are different, ask for them to type again until a right value is given. .

sex = str(input('inform your sex: [m/f]: ')).strip().upper()[0]
while sex != 'M' and sex != 'F': # aqui dava para por *while* sex *not in* 'MmFf':
    sex = str(input('invalid data. please, inform your sex: ')).strip().upper()[0]
print(f'sex {sex} successfully saved')
