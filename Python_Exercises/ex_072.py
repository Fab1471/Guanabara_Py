# Create a program that has a Tuple written out in full totally fulfilled with a count from 0 to 20.

# Your program should read a number through the keyboard (among 0 and 20) and write it out in full.

infull = ('zero', 'one', 'two', 'three', 'four',
 'five', 'six', 'seven', 'eight', 'nine', 'ten',
  'eleven', 'twelve', 'thirteen', 'fourteen',
   'fifteen', 'sixteen', 'seventeen',
    'eighteen', 'nineteen', 'twenty')
while True:
    while True:
        n = int(input('type a number among 0 and 20: '))
        if 0 <= n <= 20:
            break
        print('try again.', end=' ')
    print(f'you typed the number {infull[n]}') # vai mostrar o infull(extenso) de n(number). .
    proceed = ' '
    while proceed not in 'yn':
        proceed = str(input('do you want to proceed? [y/n] ')).strip().lower()[0]
    if proceed == 'n':
        break
print('end of the program. .')
