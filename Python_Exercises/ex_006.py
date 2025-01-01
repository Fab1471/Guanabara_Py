#Create an algorithm that reads a number and show it's double, triple and square root.
gn = int(input('type a number: '))
db = (gn*2)
tp = (gn*3)
sr = gn**(1/2)
print(f"the number is, {gn}. \nit's double is, {db}. \nit's triple is, {tp}. \nit's square root is, {sr:.2f}")
# colocar :.f2 faz com q ele formate para ter apenas 2 casa de float. 
# dois pontos, ponto, f de float e o número de casas flutuantes desejadas. .
# a raiz quadrada tb dá pra fazer de outro jeito, usando a função power (pow) de potência, ficando 
#pow(gv,1/2)
print('pow(gn,(1/2)') #tentar arrumar essa sqr root aqui dps. .
