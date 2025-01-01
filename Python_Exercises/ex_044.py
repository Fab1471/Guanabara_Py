# Elaborate a program that calculate the value to be paid for a product, considering 
# it's [normal price] and the [condition of payment].

# in cash, check -  10% of discount
# 1x card - 5% discount
# 2x card - regular price
# 3x card or more - 20% of interest

print(f'{" Lojas Milena ":=^40}')
rprice =  float(input('what is the price of the product? R$ '))
print('''Payment Methods
[1] in cash
[2] 1x credit card
[3] 2x credit card
[4] 3x 'plus' credit card''')
option = int(input('what is the option? '))
if option == 1:
    total = rprice - (rprice*10/100)
elif option == 2:
    total = rprice - (rprice*5/100)
elif option == 3: 
    total = rprice
    installment = rprice/2
    print(f'Your purchase will be paid in 2 installments with no interests of R${installment:.2f}')
elif option == 4: 
    total = rprice + (rprice*20/100)
    tinst = int(input('how many installments? '))
    installment = total/tinst
    print(f'Your purchase will be paid in {tinst} istallments with interests of R${installment:.2f}')
else:
    total = rprice
    print('Wrong payment option. Please, try again.')
print(f'Your purchase of R${rprice:.2f} will cost {total:.2f} at the end. .')

'''print(f'In cash the value would be: R$ {rprice-total:.2f}')
print(f'Paying with a credit card with no installments the value would be: R$ {rprice-total:.2f}')
print(f'Paying with a credit card in 2 installments the value would be: R$ {rprice:.2f}')
print(f'Paying with a credit card in 3 installments the value would be: R$ {rprice+card3x:.2f}')'''

'''

com a nova formatação do format, que usa apenas (f), 
você deve escrever o nome da loja ou o texto que desejar ANTES 
dos dois pontos e com novas aspas que sejam aspas diferentes da que usou no começo. 
No exemplo do vídeo, ficaria assim:

print(f'{"Lojas Gunabara":=^40}')

'''
