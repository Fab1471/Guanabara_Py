g1 = float(input('type the 1st grade: '))
g2 = float(input('type the 2nd grade: '))
av = (g1+g2)/2
print(f'Your average was {av:.1f}')
if av >= 6.0:
    print('Your average was good. Keep it up!')
else:
    print('Your average was bad. Study more!')
