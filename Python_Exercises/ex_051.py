# Develop a program that read the 1st term and the ratio of an arithmetic progression.
# At the end, show the 10 first numbers of this progression.

print('=*='*7)
print('Arithmetic Progression')
print('=*='*7)
first = int(input('1st term: '))
reason = int(input('reason: '))
tenth = first + (10-1) * reason # fórumla do enésimo termo de uma p.a. .
for c in range(first, tenth + reason, reason):
    print(f'{c}', end='...')
print('end')
