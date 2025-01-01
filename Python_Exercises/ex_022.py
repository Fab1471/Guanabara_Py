# Create a program which reads the full name of a person and show: 
# The name with all the letters being Capital Letters
# The name with all the letters being Lower Case Letters
# How many letters there are in the name, not considering the spaces. .
# How many letters has the first name got.

name = str(input('What is your name? ')).strip()
print('Analysing your name. .')
cname = name.upper()
lname =  name.lower()
print(f'Your name in capital letters would be: {cname}') # upper
print(f'Your name in lower case letters would be: {lname}') # lower
print(f'Your name in capital letters would be: {name.upper()}') # upper
print(f'Your name in lower case letters would be: {name.lower()}') # lower

total = len(name)-name.count(' ')
print(f'Your name has a total of {total} letters.') # deu pra arrumar. .
print(f"Your name has a total of {(len(name)-name.count(' '))} letters") # tive q usar aspas duplas. .

frstt = name.find(' ')
print(f"Your 1st name's got a total of {name.find(' ')} letters.")
print(f"Your 1st name's got a total of {frstt} letters.")

#print('Your name has a total of {} letters'.format(len(name)-name.count(' '))) guanabara way

divided = name.split()
print(f"Your 1st name's {divided[0]} and has a total of {len(divided[0])} letters")
