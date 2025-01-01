# Write a program that read 2 int numbers and compare them. Showing at the screen a messagem:
# the 1st value is bigger
# the 2nd value is bigger
# there is no bigger value, they're both the same

n1 = int(input('1st number: '))
n2 = int(input('2nd number: '))
if n1 > n2:
    print('1st number is the bigger')
elif n2 > n1:
    print('2nd number is the bigger')
elif n1 == n2:
    print('there is no bigger value, they are both the same')
# daria tb para lançar o else e não discriminar igualidade. .
