print('weight, mass and fat %')
weight = float(input('weight: '))
mass = float(input('mass: '))
fat = weight - mass
masspct = (mass/weight) * 100
fatpct = (fat/weight) * 100
print(f'mass: {masspct:.2f}%')
print(f'fat: {fatpct:.2f}%')
