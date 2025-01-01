test = list()
test.append('Gustavo')
test.append(40)
dudes = list()
dudes.append(test[:])
test[0] = 'Maria'
test[1] = 22
dudes.append(test[:])
print(test)
print(dudes)
