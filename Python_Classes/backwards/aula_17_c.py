a = [2, 3, 4, 7]
b = a # when you do that you connect the 2 lists together. . unless you do the other way below. .
b[2] = 8 
print(f'A list: {a}')
print(f'B list: {b}')


a = [2, 3, 4, 7]
b = a[:] # and when you execute, you see that the 4 in the 1st list remains in this case bc it was a copy and not a bond. .
b[2] = 8 
print(f'A list: {a}')
print(f'B list: {b}')
