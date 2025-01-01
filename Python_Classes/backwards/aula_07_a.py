print('='*50)
name = input('What is your name?')
print (f"Nice to meet you, {name}")
n1 = int(input('1st value: '))
n2 = int(input('2nd value: '))
#print(f'the sum is, {n1+n2}')
#se usar variável é pq provavelmente vc vai precisar de usar o resultado depois. .
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print(f'the sum is: {s} the product is: {m} the division is: {d:.3f}', end=' ,') #aqui o :.3f para mostrar apenas 3 de float. .
print(f'the total div is: {di}, the potency is: {e}')

#\n quebra a linha. .
#end= '' qlq coisa dentro das aspas, pula linha. podendo inclusive ser vazio. .
