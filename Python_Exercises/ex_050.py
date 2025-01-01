# Develop a program that read 6 int numbers and show the sum only of the ones that are even.
# If the typed value is odd, disconsider it.

sum = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'type the {c}° value: '))
    if num %2 == 0:
        sum+= num
        cont+= 1
print(f'you informed {cont} even numbers and the sum was {sum}')
