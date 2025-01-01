# Create a program that read the name and the price of several products.
# The program must ask if the user will continue.
# At the end show:

# A: what is the total spend at the purchase
# B: how many products cost more than 1000 reals
# C: what is the name of the cheapest product

tspend = tthousand = lprice = count = 0
cheapest = ' '
print("Astronaut's Shop")
while True:
    product = str(input('product: '))
    price = float(input('price: R$'))
    count+=1
    tspend+=price
    if price > 1000:
        tthousand+=1
    if count == 1 or price < lprice:
        lprice = price
        cheapest = product
    buymore = ' '
    while buymore not in 'yn':
        buymore= str(input('do you want to continue shopping? [y/n] ')).strip().lower()[0]
    if buymore == 'n':
        break
print(f'the total spend at the purchase was R${tspend:.2f}')
print(f'the quantity of products above a thousand reals is {tthousand}')
print(f'the cheapest product was the {cheapest} that cost R${lprice:.2f}')
