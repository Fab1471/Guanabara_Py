# Create a program that read several int numbers through the keyboard.
# The program will just stop when the user type the value 999, which is the stop condition.
# At the end, show the quantity of numbers that were typed and the sum between them.    
# Not considering the flag.

n = ' '
q = 0
s = 0
n = int(input('type a number [999 to stop]: ')) # tentar entender exatamente oq aconteceu aqui 
while n != 999:
    q+=1
    s+=n
    n = int(input('type a number [999 to stop]: ')) # com essa adição da mesma linha 2x. .
print(f'the quantity of numbers typed was: {q}')
print(f'the sum of the typed numbers was: {s}')
