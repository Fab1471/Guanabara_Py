#Make a program which reads any int number and show on the screen it's multiplication table. 

n0 = int(input("type a number to see it's multiplication table: "))
n1 = n0*1
n2 = n0*2
n3 = n0*3
n4 = n0*4
n5 = n0*5
n6 = n0*6
n7 = n0*7
n8 = n0*8
n9 = n0*9
nt = n0*10

print('-------------------------------------------------')
print(f'the multiplication table of the number {n0} is: \n--------------------------------------------- \n\n{n0} x  1 = {n1}\n{n0} x  2 = {n2}\n{n0} x  3 = {n3}\n{n0} x  4 = {n4}\n{n0} x  5 = {n5}\n{n0} x  6 = {n6}\n{n0} x  7 = {n7}\n{n0} x  8 = {n8}\n{n0} x  9 = {n9}\n{n0} x 10 = {nt}')
print('---------------------------------------------')

#print(f'{n0} x {1:2} = {n1}') outra maneira de fazer com todos em format, rs. .
#print('-'*40) coloca oq vc qr q apareça dentro das aspas [*vezes*] o número de vezes desejadas. .
