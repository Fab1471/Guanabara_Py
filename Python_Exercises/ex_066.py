# Create a program that reads several int numbers through the keyboar.
# The program will just stop when the user types the value 999, which is the condition to stop.
# At the end show how many numbers were typed and which was the sum among them.
# Disconsidering the flag!

vq = 0
sum = 0
while True:
    value = int(input('type a value (999 to stop): '))
    if value == 999:
        break
    vq+=1
    sum += value
print(f'the quantity of typed numbers was {vq} and the sum among them equals {sum}')

# while tem teste lógico no início?
