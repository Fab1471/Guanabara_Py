# Create a program that read any phrase and tells if it is a palindrome, not considering the spaces. 

# Após a Sopa
# A Sacada da Casa
# A Torre da Derrota
# O Lobo Ama o Bolo
# Anotaram a Data da Maratona

phrase = str(input('type a phrase: ')).strip().upper()
words = phrase.split()
together = ''.join(words)
# inversion = '' removi pra testar sem o for
inversion = together[::-1]
'''for letter in range(len(together) -1, -1, -1):
    inversion+=together[letter]''' # removido para testar sem o for
# print(together, inversion)
print(f'the inversion of {together} is {inversion}')
if inversion == together:
    print('we have a palindrome')
else:
    print('the typed phrase is not a palindrome')
