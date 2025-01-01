# Create a program that reads the age and sex of several ppl. 
# To each person registred, the program must ask if the user wants to continue or not.
# At the end, shows:

# A: how many ppl are over 18 
# B: how many men were registred
# C: how many women are below 20 

over18 = totmen = totwomen = 0
while True:
    age = int(input('age: '))
    sex = ' '
    while sex not in 'mf':    
        sex = str(input('sex: [m/f] ')).strip().lower()[0]
    if age >= 18:
        over18+=1
    if sex == 'm':
        totmen+=1
    if sex == 'f' and age < 20:
        totwomen+=1
    proceed = ' '
    while proceed not in 'yn':
        proceed = str(input('do you want to proceed? [y/n] ')).strip().lower()[0]
    if proceed == 'n':
        break
print(f'there are {over18} ppl over 18')
print(f'there are {totmen} men registred in the program')   
print(f'there are {totwomen} women registred in the program under 20 years old')
