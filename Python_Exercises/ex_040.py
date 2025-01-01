# Create a program that read 2 grades of a student and give it's average, showing a message at the end,
# taking into account the average reached.

# average under 5.0: reproved
# betweeen 5.0 and 6.9: recovery
# 7 or above: approved

g1 = float(input('1st grade: '))
g2 = float(input('2nd grade: '))
av = (g1+g2)/2
if av<5:
    print('reproved')
elif av >=5 and av <=6.9:
    print('recovery')
elif av>=7:
    print('approved')
print(f'bc your average was: {av:.1f}')
# if 7 > av >= 5:
