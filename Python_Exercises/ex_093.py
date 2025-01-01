# Create a program that manages the use of a soccer player. The program will read the name of the player and how many matches he played.
# After that will read the quantity of goals made in each match. Athe the end, all of that will be saved in a dictionary,
# including the total of goals made during the championship.

player = dict()
matches = list()
player['name'] = str(input("Player's Name: "))
tot = int(input(f'How many matches {player["name"]} played? '))
for c in range(0, tot):
    matches.append(int(input(f'How many goals at the match {c}? ')))
player['goals'] = matches[:]
player['total'] = sum(matches)
print('-='*30)
print(player)
print('-='*30)
for k, v in player.items():
    print(f'The field {k} has the value of {v}')
print('-='*30)
print(f'The player {player["name"]} played {len(player["goals"])} matches.')
for i, v in enumerate(player['goals']):
    print(f'    => At the match {i}, did {v} goals.')
print(f'Having a total of {player["total"]} goals')
