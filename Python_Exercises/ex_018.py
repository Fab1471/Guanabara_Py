# Make a program that reads any angle and shows at the screen the value of it's: 
# sine, cosine and tangent of it's angle. .

# eixo vertical = senos
# eixo horizontal = cossenos
# no círculo trigonométrico
# a tangente é uma linha q vai passar tangenciando o ponto referente ao angulo indicado

from math import radians, sin, cos, tan
ang = float(input('type the desired angle: '))
# ele vai me dar o seno em radianos, terá q converter. .
sin = sin(radians(ang)) # digita um valor, converte pra radianos e calcula o seno dele. .
cos = cos(radians(ang))
tan = tan(radians(ang))

print(f'The angle of {ang} has the sin of {sin:.2f}')
print(f'The angle of {ang} has the cos of {cos:.2f}')
print(f'The angle of {ang} has the tan of {tan:.2f}')
