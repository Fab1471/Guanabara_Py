# Create a program that has an only Tuple with names of products and 
# it's respectives prices in the sequence.

# At the end, show a list of prices organizing the data in a Tabular form.

tp = ('Pencil', 1.75, 
'Eraser', 2, 
'Notebook', 15.90, 
'Pencil Case', 25, 
'Transfer', 4.20, 
'Compass', 9.99, 
'Backpack', 120.32, 
'Pens', 22.30, 
'Book', 34.90)
print('-'*40)
print(f'{"Price List":^40}')
print('-'*40)
for pos in range(0, len(tp)):
    if pos % 2 == 0:
        print(f'{tp[pos]:.<30}', end=' ')
    else:
        print(f'{tp[pos]:>7.2f}')
print('-'*40)
