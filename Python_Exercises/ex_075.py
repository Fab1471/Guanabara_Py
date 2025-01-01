# Develop a program that reads 4 values through the keyboard and insert them in a Tuple.
# At the end, show:

# a: how many times the value 9 appeared
# b: in which position was typed the first value 3
# c: which ones were the even numbers 

n = (int(input('type a number: ')), 
    int(input('type another number: ')), 
    int(input('type one more number: ')), 
    int(input('type the last number: ')))
print(f'you typed the numbers {n}')
print(f'the value 9 appeared {n.count(9)} times')
if 3 in n:
    print(f'the value 3 appeared at the {n.index(3)+1}° position') # se não tiver o index, tem q condicionar com if
else:
    print('the value 3 was not typed in any position')
print('the even numbers typed were', end=' ')
for n in n:
    if n % 2 == 0:
        print(n, end=' ')
