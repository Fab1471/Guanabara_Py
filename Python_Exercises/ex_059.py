# Create a program that read 2 values and show a menu at the screen:

# [1] sum
# [2] times
# [3] major
# [4] new numbers
# [5] exit the program

# Your program must do the demanded operation on each case.

from time import sleep
value1 = int(input('1st value: '))
value2 = int(input('2nd value: '))
option = 0
while option != 5:
    print('''\n    [1] sum
    [2] times
    [3] major
    [4] new numbers
    [5] exit the program''')
    option = int(input('\n>>>>>>> what is your option? '))
    if option == 1:
        sum = value1+value2
        print(f'the sum between {value1} and {value2} is {sum}.')    
    elif option == 2:
        times = value1*value2
        print(f'the product between {value1} and {value2} equals {times}.')
    elif option == 3:
        if value1 > value2:
            major = value1
        else:
            major = value2
            print(f'between {value1} and {value2} the highest value is {major}.')
    elif option == 4:
        print('inform the numbers again: ')
        value1 = int(input('1st value: '))
        value2 = int(input('2nd value: '))
    elif option == 5:
        print('ending the program. .')
    else:
        print('wrong option. please, try again.')
    print('=-=' *10)
    sleep(2)
print('end of the program. be welcome!')
