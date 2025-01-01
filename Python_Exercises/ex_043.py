# Develop a logic that read the weight and height of a person, caculate it's IMC and show their status,
# according with the table down here. 

# under 18.5: underweight
# betweeen 18.5 and 25: correct weight
# 25 to 30: overweight
# 30 to 40: obesity
# above 40: morbid obesity

weight = float(input('what is your weight? (kg) '))
height = float(input('what is your height? (mt) '))
imc = weight/(height)**2
if imc <18.5:
    print('underweight')
elif imc >=18.5 and imc <=25: # também daria para fazer 18.5 <= imc < 25
    print('correct weight')   # o imc é menor q 25, mas é maior ou igual doq 18.5
elif imc >=25 and imc <=40: 
    print('overweight')
elif imc <=30 and imc <=40:
    print('obesity')
else:
    print('morbid obesity')
print(f'bc your imc is {imc:.1f}')

# se eu colocar print(type(variável)) o programa vai me retonar o tipo primitivo da variável q ela contém. .
