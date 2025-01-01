phrase =  '   Curso em Vídeo Python   ' 
print(phrase) 

# qnd é pra iniciar, ele inicia uma depois.
# qnd é pra terminar, ele termina na mesma declarada.

print(phrase[3]) # 3 aqui mas, vai ser 4° letra. .  
print(phrase[3:13]) # quarta até a 13 mesmo. .
print(phrase[:13]) # aqui vai do 0 até a 13 mesmo. .
print(phrase[13:]) # aqui vai uma depois até o final. .
print(phrase[1:15]) #aqui vai ser da 2° letra, pq é uma dps. até a 14. [urso em Vídeo]
print(phrase[1:15:2]) #vai startar da 2 letra e vai pulando de 2 em 2 até a 14.
print(phrase[1::2]) # aqui vai pulando de 2 em 2 até o final, pois nada foi indicado no meio dos ::
print(phrase[::2]) # não indicado o início nem final, será a string inteira pulando de 2 em 2.
print('Hi')
print("""Trying to Back in Time""")
# frase é uma cadeia de caracteres, mas no Python tudo é um objeto.
# sendo então possível colocar alguma coisa ponto alguma coisa
print(phrase.count('o')) # pediu para contar quantas vezes tem a letra (o) = resultado 3
print(phrase.upper().count('O')) # mandando contar a qtdade de o na frase jogada pra letra maiuscula. .
print(len(phrase)) # conta a qtidade, o tamanho da frase;
print(len(phrase.strip())) # .strip remove os espaços desnecessários, no início e final.
print(phrase[0]) # parece q não tá funcionando aqui. . era pra mostrar a letra C
phrase = phrase.replace('Python', 'Android')
print(phrase)
print(phrase[3]) # não mostrou na linha 23 pq tinham alguns espaços antes de iniciarem as letras. .

# a string é imutável a não ser q ela receba um replace e dps a variável receba uma atribuição. .
print('Curso' in phrase) # me dará uma resposta booleana. .
print(phrase.find('Curso')) # a posição é 3 por causa dos espaços. .
print(phrase.lower().find('vídeo')) # a posição é 12 por causa dos espaços. .
print(phrase.split())

divided = phrase.split() # divided aqui na verdade não é uma varíavel, senão objeto. tudo é objeto.
print(divided) # divided virou uma lista
print(divided[0]) # qnd coloco 0 mostra o primeiro item da lista, 0/4 
print(divided[2][3]) # dividido 2 q é vid e mostra a 3ra letra q vai ser a 4ta qnd starta. .
