#Write a program that asks the quantity of kilometers traveled by a rental car 
#and the amount of days the car was rented for. 
#Calculate the price to pay, knowing that the car costs R$60,00 per day and R$0,15 per traveled km. .
days = int(input('For how many days was the car rented: '))
km = float(input('How many kilometers has the car traveled? '))
totaldaysprice = days*60
totalkmvalue = km*0.15
tvp = totaldaysprice+totalkmvalue
print(f'The value considering only the number of contracted days would be R${totaldaysprice:.2f}')
print(f'The total value of the kilometers traveld was R${totalkmvalue:.2f}')
print(f'The total value to pay is R${tvp:.2f}')
