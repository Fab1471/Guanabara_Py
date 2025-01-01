# Create a program where the user can type 7 numeric values and index them in on single list that keep the separated the even and the odd numbers.
# At the end show the even and odd values separeted in an ascending order. .

n = [[], []]
value = 0
for c in range(1, 8):
    value = int(input(f'type the {c}o. value: '))
    if value %2 == 0:
        n[0].append(value)
    else:
        n[1].append(value)
print('-='*30)
n[0].sort()
n[1].sort()
print(f' all values: {n}')
print(f'the even were: {n[0]}')
print(f'the odd were: {n[1]}')
