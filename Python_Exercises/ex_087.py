# Upgrade the previous exercise, showing at the end:

# A: The sum of all the even typed numbers.
# B: The sum of the values of the third column.
# C: The highest value of the 2nd line.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Type a value for [{l}, {c}]: '))
#print(matrix)
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c]%2 ==0:
            spar+= matrix[l][c]
    print()
print('-='*30)
print(f'the sum of the even numbers is {spar}')
for l in range(0, 3):
    scol+= matrix[l][2]
print(f'the sum of the values of the third column is {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matrix[1][c]
    elif matrix[1][c] > mai:
        mai = matrix[1][c]
print(f'the highest value of the 2nd line is {mai}')
