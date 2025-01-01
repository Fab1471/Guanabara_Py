# Make a program that read 5 values and keep them in a list.
# At the end, show which was the highest a lowest typed value and their respective positions at the list.

listn = []
h = 0
l = 0
for c in range(0, 5):
    listn.append(int(input(f'type a value for the position {c}: ')))
    if c == 0:
        h = l = listn[c]
    else:
        if listn[c] > h:
            h = listn[c]
        if listn[c] < l:
            l = listn[c]
print('=-'*30)
print(f'you typed the numbers {listn}')
print(f'the highest typed value was {h} at the positions ', end=' ')
for i, v in enumerate(listn):
    if v == h:
        print(f'{i}. . ', end= ' ')

print()
print(f'the lowest typed value was {l} at the positions ', end=' ')
for i, v in enumerate(listn):
    if v == l:
        print(f'{i}. . ', end=' ')
print()
