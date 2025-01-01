# Make a program that read the weight of 5 ppl.
# At the end show which one was the heaviest and the lightest readen.

heaviest = 0
lightest = 0
for person in range(1, 6):
    weight = float(input(f'weight of the {person}° person: '))
    if person == 1:
        heaviest = weight
        lightest = weight
    else:
        if weight > heaviest:
            heaviest = weight
        if weight < lightest:
            lightest = weight
print(f'the heaviest weight was {heaviest}kg')
print(f'the lightest weight was {lightest}kg')
