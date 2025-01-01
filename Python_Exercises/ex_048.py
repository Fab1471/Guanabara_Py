# Make a program that calculate the sum between all the odd numbers that are multiples of 3 in the
# interval of 1 to 500. .

sum = 0
acm = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        sum = sum + c          # o acumulador, vai acumular os números, somando. .   sum=+c dá no mesmo. .
        acm = acm +1       # contador vai receber um número mais outro, contando. .  acm=+acm dá no mesmo. .
print(f'the sum of all {acm} required values is: {sum}')
