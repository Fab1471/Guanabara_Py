from re import S


n = int(input('type a number: '))
for c in range(0, n+1):
    print(c)
print('End')


s = int(input('start: ')) # indica a variável de início
e = int(input('end: ')) # indica a variável de fim
p = int(input('step: ')) # indica o salto ou passo
for i in range(s, e+1, p): # contador i recebe no range das variáveis os cmds a serem .exe
    print(i)  # o +1 apenas faz com q pare no número indicado, ele ajusta a contagem por causa dos moldes do py
print('End')
