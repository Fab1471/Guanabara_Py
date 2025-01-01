# Create a program that creates a matrix with dimensions 3x3 and fulfill with values given through the keyboard.
# At the end, show the matrix at the screen with the correct format. .

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Type a value for [{l}, {c}]: '))
#print(matrix)
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()
