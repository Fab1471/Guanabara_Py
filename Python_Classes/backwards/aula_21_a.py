def contador(i, f, p):
    """
-> Faz uma contagem e mostra na tela.
    parâmetro i: início da contagem
    parâmetro f: fim da contagem
    parâmetro p: passo da contagem
         return: sem retorno
         Função criada por Fabri_Junin
    """
    c= i 
    while c <= f:
        print(f'{c} ', end=' ')
        c+=p
    print('Fim!')


contador(2, 10, 2)

help(contador)
