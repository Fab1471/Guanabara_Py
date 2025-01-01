n = 1
even = odd = 0  # 2 variáveis numa mesma linha com o mesmo valor. .
while n != 0:
    n = int(input('type a value: '))
    if n != 0:
        if n % 2 == 0:
            even = even +1
        else:
            odd +=1 # essa expressão [ odd+=1 ] significa q ímpar recebe ímpar +1
print(f'you typed {even} even numbers and {odd} odd numbers.')
