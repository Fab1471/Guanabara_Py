lanche = ('Hamburguer', 'Juice', 'Pizza', 'Pudding', 'French Fries') 
# nesse Python já é possível criar uma Tupla sem ()
print(lanche[1]) # na hr de referenciar sempre usamos [] 
print(lanche[1:3]) # do 1 até o 3, ignorando sempre o último. .
print(lanche[2:]) # 2: mostra do elemento 2 até o final. .
print(lanche[:2]) # :2 mostra do ínicio até o elemento 2 mas, ele irá ignorar o elemento 2. .
print(lanche[-3:]) # aqui vai do -3 q é o Pizza, até o final para a direita. .
print(len(lanche)) # mostra o comprimento, ou qts termos tem a Tupla

# Tuplas são imutáveis!
# Hamburguer, Juice, Pizza, Pudding, French Fries
#      0    ,    1  ,   2  ,   3  ,    4
#     -5    ,   -4  ,  -3  ,  -2  ,   -1

for comida in lanche:
    print(f'I will eat {comida}')

for cont in range(0, len(lanche)):
    print(f'I will eat {lanche[cont]} in {cont}° place') # mostrar o lanche na posição cont, top!
print('I ate a lot!')

for pos, comida in enumerate(lanche):
    print(f'I will eat {comida} in {pos}° place')
print('I ate a lot!')

print(sorted(lanche)) # ordenado, coloca em ordem a Tupla
