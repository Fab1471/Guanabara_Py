# Make a program that show at the screen all the even numbers into the interval between 1 and 50.

for counter in range(2, 51, 2):
    print('.', end='') # com a solução de salto, o programa utiliza menos processamento, logo, fica mais leve. .
    if counter % 2  == 0:
        print(counter, end=' ')
print('end. .')
