# Make a program that has a Function called
# counter(), that receives 3 parameters:
# start, end and pass. Your program has to
# execute 3 counts through the defined Function

# a) from 1 to 10, from 1 by 1.
# b) from 10 to 0, from 2 by 2.
# c) a personalized count.

from time import sleep

def counter(s, e, p):
    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Result of counting from {s} to {e} counting {p} by {p}. ')
    sleep(2.5)
    
    if s < e:
        cont = s
        while cont <=e :
            print(f'{cont} ', end= ' ')
            sleep(0.5)
            cont +=p
        print('The End. .')
    else:
        cont = s
        while cont >= e:
            print(f'{cont} ', end= '')
            sleep(0.5)
            cont -= p
        print('End!')

# Programa Principal
counter(1, 10, 1)
counter(10, 0, 2)
print('-='*20)
print('Now is your time to personalize the counter!')
sta = int(input('Start: '))
end = int(input('End:   '))
pace = int(input('Pass: '))
counter(sta, end, pace)
