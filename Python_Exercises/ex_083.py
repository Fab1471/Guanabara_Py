# Create a program where the user types any expression using (). 
# Your application must analyse if the expression is with the () oppened and closed in the correct order. . 

expr = str(input('type a expression: '))
pile = []
for simb in expr:
    if simb== '(':
        pile.append('(')
    elif simb == ')':
        if len(pile) > 0:
            pile.pop()
        else: 
            pile.append(')')
            break
if len(pile) == 0:
    print("you've got a valid expression")
else:
    print('this expression is not valid')
