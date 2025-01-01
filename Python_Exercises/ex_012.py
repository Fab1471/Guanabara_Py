#Make an algorithm that reads the price of a product and shows it's new price with 5% of discount. .
price = float(input('What is the price of the product? '))
disc = price*5/100
discprice = price-disc
print(f'The price of this product with 5% off is: {discprice:.2f}')
