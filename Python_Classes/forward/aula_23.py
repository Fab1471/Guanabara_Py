# Curso Python #23 - Tratamento de Erros e Exceções

'''

A semântica, no contexto da programação de computadores, refere-se ao significado do código, ou seja, o que o programa está fazendo. 
Enquanto a sintaxe se preocupa com a estrutura gramatical e as regras de formação do código, a semântica está relacionada ao significado
 e à interpretação do código.

Por exemplo, se um programa está escrito corretamente em termos de sintaxe, mas a lógica interna não faz sentido ou produz resultados 
indesejados, estamos falando de problemas semânticos. Erros semânticos podem incluir lógica incorreta, manipulação inadequada de dados, 
ou qualquer situação em que o programa não esteja se comportando conforme o esperado.

Corrigir erros semânticos geralmente envolve uma compreensão mais profunda da lógica do programa e do problema que está sendo resolvido. 
Ferramentas de depuração, como impressão de mensagens e análise cuidadosa do código, são frequentemente usadas para identificar e 
corrigir problemas semânticos.

Em resumo, enquanto a sintaxe está relacionada à estrutura gramatical correta do código, a semântica se concentra no significado e 
na lógica do programa. Ambos são aspectos críticos no desenvolvimento de software.


'''

# Sintaxe = gramática/grafia
# Semântica = significado/comando

# qnd não é sintático temos uma exceção. .

# NameError = por exemplo. .

# ValueError = erro de valor 
# e.g = esperava int e recebeu um str

# ZeroDivisionError
# TypeError
# IndexError []
# KeyError {}
# ModuleNotFoundError

'''
try:
    operação
except:
    falhou
else:
    deu certo
finally:
    certo/falha

'''

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print('\n :/ [Infelizmente tivemos  um Problema] :/ \n')
    print(f'O problema encontrado foi {erro.__class__}\n')
else:
    print(f'\nO resultado é {r:.1f}\n')
finally:
    print(' Volte sempre!\n Muito obrigado!\n')





# um mesmo try pode ter vários except. .
    
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'\nO resultado é {r:.1f}\n')
finally:
    print(' Volte sempre!\n Muito obrigado!\n')
