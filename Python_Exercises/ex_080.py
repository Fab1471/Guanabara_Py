# Create a program where the user can type 5 numeric values and insert them in a list, already in the correct position.
# (not using sort() )
# At the end, show de ordered list displayed at the screen.

list = []
for c in range(0, 5):
    n = int(input('type a number : '))
    if c == 0 or n > list[-1]:
        list.append(n)
        print('added to the end of the list')
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                print(f'added at the position {pos} of the list')
                break
            pos+=1
print('-='*30)
print(f'the typed values in order were {list}')
