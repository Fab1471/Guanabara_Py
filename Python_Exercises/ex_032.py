# Make a program that reads any year and shows if it's a leap year.

from datetime import date
year = int(input('Which year would you like to analyse? '))
if year == 0: 
    year = date.today().year # pra se colocar 0 rodar o ano atual. .
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'The year {year} is a leap year.')
else:
    print(f'The year {year} is not a leap year')

'''

"ano % 4 == 0" diz que todos os anos divisíveis por 4 são bissextos (2008, 2012, 2016, 2020 etc)

"ano % 100 != 0" diz que todos os anos divisíveis por 100 NÃO são bissextos, criando "falhas" na sequência (retira-se os anos 1700, 1800, 1900, 2000 etc)

"ano % 400 == 0" preenche as falhas com somente os números divisíveis por 400 (800, 1200, 1600, 2000 etc)

Então "ano % 4 == 0 and ano % 100 != 0" é um critério, e "ano % 400 == 0" é outro.

'''
