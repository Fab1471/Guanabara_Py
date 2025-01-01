# Develop a program that ask the distance of a trip in km.
# Calculate the price of the ticket, charging R$0,50 per km to trips untill 200km and
# R$0,45 for further trips. 

distance = float(input('What is the distance of the trip? '))
print(f'You are about to begin a trip of {distance} kilometers. . ')
if distance <=200:
    price = distance*0.50
    
    
else: 
    price =  distance*0.45
print(f'And the price of your ticket will be: R${price:.2f}')

from time import sleep

print('Processing test 2. .') # tem q arrumar, não tá mostrando a segunda opção. .
sleep (2)

distance = float(input('What is the distance of the trip? '))
if distance <=200:
    price = distance*0.50
    print(f'You are about to begin a trip of {distance} kilometers. . ')
    print(f'And the price of your ticket will be: R${price:.2f}')
elif distance >200: 
        price2 =  distance*0.45
        (f'You are about to begin a trip of {distance} kilometers. . ')
        (f'And the price of your ticket will be: R${price2:.2f}')
