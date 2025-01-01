# Make a program that has a Function called largest(),
# that receives several parameters with integer
# values. Your program has to parse all the
# values and indicate which one of them is the largest.

from time import sleep

def largest(* num): # parâmetros empacotados (uso asterísco)
    cont = largest = 0
    print('-='*30)
    print('Parsing the received values. .')
    for value in num:
        print(f'{value} ', end='')
        sleep(0.3)
        if cont == 0:
            largest = value
        else:
            if value > largest:
                largest = value
        cont +=1
    print(f'In total, {cont} values were received. ')
    print(f'The largest informed value was {largest}. ')


# Main Program
largest(2, 9, 4, 5, 7, 1)
largest(4, 7, 0)
largest(1, 2)
largest(6)
largest()
