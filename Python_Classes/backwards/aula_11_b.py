from stat import FILE_ATTRIBUTE_INTEGRITY_STREAM


a = 3
b = 5
print(f'The values are \033[32m{a}\033[m and \033[31m{b}\033[m')

name = 'Fabri'
colors = {'clear':'\033[m',     # foi criado um padrão de cor rápida para poder ser aplicado dentro do print. .
 'blue':'\033[34m',
 'yellow':'\033[33m',
  'blacknwhite':'\033[7:30m'}
print(f"Hello! Very pleased to meet you, \033[4;34m{name}\033[m.")

print(f"testing the colours we have this one here, {colors['yellow']}{name}{colors['clear']}. And also that other one right here too {colors['blacknwhite']}{name}{colors['clear']}. .")
# aspas duplas quando a sintaxe não fechar. .

print('testing the colours we have this one here, {}{}{}. And also that other one right  here too{}{}{} . .'.format(colors['yellow'], name, colors['clear'], colors['blacknwhite'], name, colors['clear']))


colors['yellow']

colors['clear']

colors['blacknwhite']

colors['clear']
