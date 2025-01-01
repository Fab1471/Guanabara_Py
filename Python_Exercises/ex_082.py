# Create a program that will read several numbers and put them in a list.

# After that, create 2 extra lists that will have just the even and odd values respectively typed.

# At the end, show the content of the 3 generated lists.

num = list()
evens = list()
odds = list()
while True:
    num.append(int(input('type a number: ')))
    answer = str(input('wanna continue? [y/n] '))
    if answer in 'Nn':
        break
for i, v in enumerate(num):
    if v%2 == 0:
        evens.append(v)
    elif v%2 ==1:
        odds.append(v)
print('-='*30)
print(f'the complete list is {num}')
print(f'the even list is: {evens}')
print(f'the odd list is {odds}')
