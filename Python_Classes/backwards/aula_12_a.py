name = str(input('What is your name? '))
print(f'Have a good day, {name}')
if name == 'Fabri':
    print("What a beautiful name you've got!") # até aqui temos uma condição simples
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo': # a partir do elif já temos uma cond aninhada. .
    print('Your name is very popular in Brazil')
elif name in 'Milena Ana Cláudia Jéssica Juliana':
    print('Beautiful feminine name!')
else: # a partir deste else já temos uma condição composta
    print ('Your name is pretty commom.') 
