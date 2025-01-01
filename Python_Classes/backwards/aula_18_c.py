dudes = list()
data = list()
totmai = totmen = 0
for c in range(0, 3):
    data.append(str(input('Name: ')))
    data.append(int(input('Age: ')))
    dudes.append(data[:])
    data.clear()
print(dudes)
for p in dudes:
    if p[1] >= 21:
        print(f'{p[0]} is over 18')
        totmai +=1
    else: 
        print(f'{p[0]} is under 18')
        totmen +=1
print(f'there are {totmai} over 18 and {totmen} under 18')
