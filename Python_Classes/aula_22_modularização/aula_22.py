# Modularização é o ato de construir Módulos

# Surgiu no início da década de 60. .

# Sistemas ficando cada vez maiores. .

# Foco: dividir um programa grande. .

# Foco: aumentar a legibilidade!

# Foco: facilitar a manutenção!

# Organização do código!

# Ocultação de código detalhado. .

# Eu não preciso saber o que faz tal coisa, apenas que tal coisa faz tal coisa, kk. .

# Reutilização em outros projetos. .


def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


num = int(input('Digite um valor: '))
fat=fatorial(num)
print(f'O fatorial de {num} é {fat} ')
print(f'O dobro de {num} é {dobro(num)} ')


# pacotes e/ou bibliotecas. .
