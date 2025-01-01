# Make a program that has a list called numbers
# and two functions called sort() and evenSum().
# The 1st functions will sort 5 numbers and will
# put them inside a list and the 2nd function will
# show the sum among, all the sorted values
# that are even, by the previous function.

from random import randint
from time import sleep


def sort(list):
    print('Sorting 5 values of the list! ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        list.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print(' Done!')


def evenSum(list):
    sum = 0
    for value in list:
        if value % 2 == 0:
            sum += value
    print(f'Adding the even values of {list}, we have {sum}')


numbers = list()
sort(numbers)
evenSum(numbers)
print(numbers)
