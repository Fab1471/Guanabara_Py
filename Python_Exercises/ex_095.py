# Upgrade the 93th challenge so that it works with several players, including a system of visualization of details of the use of each player.

team = list()
player = dict()
matches = list()
    
while True:    
    player.clear()
    player['name'] = str(input("Player's Name: "))
    tot = int(input(f'How many matches {player["name"]} played? '))
    matches.clear()
    for c in range(0, tot):
        matches.append(int(input(f'How many goals at the match {c+1}? ')))
    player['goals'] = matches[:]
    player['total'] = sum(matches)
    team.append(player.copy())
    while True:
        option = str(input('Wanna continue? [Y/N]: ')).upper()[0]
        if option in 'YN':
            break
        print('ERROR! Answer only Y or N! ')
    if option == 'N':
        break
print('-='*30)
print('cod ', end=' ')
for i in player.keys():
    print(f'{i:<15}', end=' ')
print()
print('-'*40)
for k, v in enumerate(team):
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-'*40)
while True:
    search = int(input('Show date of which player? (999 stops!) '))
    if search == 999:
        break
    if search >= len(team):
        print(f'ERROR! There is not a player with code {search}! ')
    else:
        print(f' -- Showing Player {team[search]["name"]}: ')
        for i,g in enumerate(team[search]['goals']):
            print(f'     At the match {i+1} did {g} goals. ')
    print('-'*30)
print('Be Welcome!')


# World 3 was composed of:

# 1 Tuplas Class
# 2 Lists Class
# 1 Dict Class
