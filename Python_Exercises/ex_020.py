# The same professor from the previous challenge wants to draw the order 
# of the presentation of the students.
# Make a program that reads the name of those 4 students and show the order drawn. .

import random
n1 = str(input('1st name: '))
n2 = str(input('2nd name: '))
n3 = str(input('3rd name: '))
n4 = str(input('4th name: '))
list = [n1, n2, n3, n4]
random.shuffle(list) #shuffle = embaralhar
print(list)

from random import shuffle
n1 = str(input('1st name: '))
n2 = str(input('2nd name: '))
n3 = str(input('3rd name: '))
n4 = str(input('4th name: '))
list = [n1, n2, n3, n4]
shuffle(list) #shuffle = embaralhar
print(list)
