values = []
values.append(5)
values.append(9)
values.append(4)

for cont in range(0, 5):
    values.append(int(input('type a value: ')))

for c, v in enumerate(values):
    print(f'at the position {c} there is {v}. .')
print('that is the end of the list')
