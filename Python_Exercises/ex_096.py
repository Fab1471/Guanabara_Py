# Make a program that has a Function called
# area(), that receives the dimensions of a 
# rectangular field (width and length) and show the area of the field.

def area(width, length):
    a = width*length
    print(f'the area of a field {width} x {length} is {a}m². ')


print('Field Control')
print('-'*20)
w = float(input('width (m) '))
l = float(input('length (m) '))
area(w, l)
