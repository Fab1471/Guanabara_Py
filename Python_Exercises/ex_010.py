#Make a program which reads how much money someone has in the wallet 
#and how many dollars they can buy with it.
#consider 1 dolar equals 5.27 reals. .
money = float(input('How much money do you have? (BRL) '))
rate = money/5.27
print(f'With that amount of BRL you can buy {rate} USD')
#talvez aprimorar o programa e fazer com q ele conversa tb ao reverso e ou em outras moedas. .
