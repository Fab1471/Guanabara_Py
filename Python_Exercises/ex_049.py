# Remake the exercise 009, showing a multiplication table of a number that the user gives but,
# now using the for loop.

n = int(input("type a number to view it's multiplication table: "))
for v in range(1, 11):
    r=n*v
    print(f'{n} x {v:2} = {r}')
