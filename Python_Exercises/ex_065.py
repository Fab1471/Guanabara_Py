# Create a program that reads several int numbers through the keyboard. 
# At the end of the execution, show the average among them all and which one was
# the highest and the lowest readen value. 
# The program must ask the user if they want or not keep typing values.

answer = 'y'
sum = 0
vq = 0
average = 0
highest = 0
lowest = 0
while answer in 'Yy': 
    n = int(input('type a number: '))
    sum+=n
    vq+=1
    if vq == 1:
        highest = lowest = n
    else:
        if n > highest:
            highest = n
        if n < lowest:
            lowest = n
    average = n    
    
    answer = str(input('wanna proceed? [y/n] ')).upper().strip()[0] # os parenteses com 0 significa para considerar só a primeira letra. .
average = sum/vq
print(f'You typed {vq} numbers and the average was {average}')
print(f'The highest value was {highest} and the lowest was {lowest}')
