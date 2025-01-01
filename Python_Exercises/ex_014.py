#Write a program that converts a temperature from  Celsius C° to Fahrenheit F°
c = float(input('Inform the temperature in C°: '))
f = ((c*9)/5)+32 # é possível espaçar operadores sem problemas na sintaxe, analisar se é viável. .
print(f'The temperature of {c} C° is equivalent to {f} F°')
