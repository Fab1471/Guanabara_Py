num = (2, 5, 9, 1)  # tuple
print(num) # tuple

num = [2, 5, 9, 1] # list
num[2] = 3 # list
num.append(7) # list add number command
num.sort(reverse=True) # coloca em ordem os numbers
num.insert(2, 0)
if 4 in num:
    num.remove(4)
else:
    print('there is no 4')
num.pop(2)
num.remove(7)
print(num) # list
print(f'this list has {len(num)} elements.')
