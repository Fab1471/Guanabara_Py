# Create a program that simulates the operation of an ATM.
# At the start, ask the user what will be the value to be withdrawn (int number)
# and the program will inform how many banknotes of each value will be delivered.

# obs: consider that the cashier has banknotes of R$50, R$20, R$10 and R$2. .

print('='*30)
print("Astronauta's Bank")
print('='*30)
value = int(input('how much money would you like to withdraw: R$'))
total = value
note = 50
tnote = 0
while True:
    if total >= note:
        total -= note
        tnote+=1
    else:
        if tnote > 0:
            print(f'total of {tnote} notes of R${note}')
        if note == 50:
            note = 20
        elif note == 20:
            note = 10
        elif note == 10:
            note = 2
        tnote = 0
        if total == 0:
            break
print('='*30)
print("Come whenever you want to the Astronauta's bank!")
print('Have a nice day!')
