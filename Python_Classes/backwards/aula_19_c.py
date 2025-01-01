state = dict()
brasil = list()
for c in range(0, 3):
    state['uf'] = str(input('District: '))
    state['Acronym'] = str(input('Acronym: '))
    brasil.append(state.copy())
print(brasil)
for s in brasil:
    print(s)
    for k, v in s.items():
        print(f'field {k} has value {v}.')
