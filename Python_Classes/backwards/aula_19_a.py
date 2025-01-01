ppl = {'name': 'Gustavo', 'sex': 'M', 'age': '22'}
ppl['name'] = 'Leonard'
ppl['weight'] = 'lightweight'
#del ppl['sex']
print(f'{ppl["name"]} has {ppl["age"]} years. ')

# referenciar, colchetes | declarar, chaves

print(ppl.keys())
print(ppl.values())
print(ppl.items())

for k, v in ppl.items():
    print(f'{k} = {v}')
