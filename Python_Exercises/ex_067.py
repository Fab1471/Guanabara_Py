# Make a program that show the multiplication table of several numbers, once at a time, for each 
# value typed by the user.
# The program will be interrupted when the requested number is negative.

while True:
    value = int(input('do you wanna see the multiplication table of which number? '))
    print('-'*30)
    if value < 0:
        break
    for i in range(1, 11):
        print(f'{value} x {i} = {value*i}')
    print('-'*30)
print('program multiplication table over; be welcome!')
