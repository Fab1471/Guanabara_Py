'''

\033[0;30;41m # estilo nulo, letra branca, fundo vermelho
\033[4;33;44m # estilo sublinhado, letra amarela, fundo azul
\033[1:35:43m # estilo negrito, letra roxa, fundo amarelo
\033[30:42m # estilo padrão, letra branca, fundo verde
\033[m # configuração padrão do terminal
\033[7:30m # estilo negativo com letra branca, vai inverter e deixar a letra preta com fundo branco

style               text                    background
 
0  none             30      black          preto     40
1  bold             31      red            vermelho  41
4  underline        32      green          verde     42
7  negative         33      yellow         amarelo   43
                    34      blue           azul      44
                    35      Magenta        Magenta   45
                    36      cyan           ciano     46
                    37      grey           cinza     47
                    97      white          branco    107

'''

print('Hello World')
print('\033[31mHello World')
print('\033[1;31;43mHello World\033[m')
print('\033[4;29;45mHello World\033[m')
print('\033[97mHello World\033[m') # parece q tá igual a de baixo
print('\033[37mHello World\033[m') # parece q tá igual a de baixo
print('\033[7;97mHello World\033[m')
print('\033[1;33;44mHello World\033[m') # letra amarela, fundo azul
print('\033[7;33;44mHello World\033[m') # inverte, letra azul, fundo amarelo

# pesquisar o tal do colorize em hexadecimal?

'''

Atualizando 11/09/2022

text                    background
 
30      black          preto      40
31      red            vermelho   41
32      green          verde      42
33      yellow         amarelo    43
34      blue           azul       44
35      Magenta        Magenta    45
36      cyan           ciano      46
37      grey           cinza      47
97      white          branco     107

'''
