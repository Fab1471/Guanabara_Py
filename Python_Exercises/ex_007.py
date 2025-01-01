#Develop a program which reads the 2 results of a student and calculate the average between them.
g1 = float(input('grade 1: '))
g2 = float(input('grade 2: '))
grade = g1+g2
avrg = (g1+g2)/2
print(f'total grade: {grade}. the average is, {avrg:.1f}.')
# :.1f (dois pontos, ponto 1 f para mostrar 1 digito flutuante, apenas. .)
