def contador(*núm):
    for valor in núm:
        print(f'{valor} ', end=' ')
    print('Fim!')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
