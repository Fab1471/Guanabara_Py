n1 = int(input('1st value:'))
print(type(n1))
n2 = int(input('2nd value'))
print(type(n2))
sum = n1+n2
print('the sum is:', sum)
print('up above we have a simple solution')
print('down here we have a more explained formula')
#print('the sum between', n1, 'and', n2, 'is:', sum) - [working but, long]
#print(f'The sum between {} and {} is {}'.format(n1, n2, sum)) - [not used anymore]
#print(f'The sum between {1} and {2} is {sum}'.format(n1, n2, sum)) - [errors fulfilling]
print(f'The sum between {n1} and {n2} is {sum}')
