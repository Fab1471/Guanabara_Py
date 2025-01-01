# Create a Tuple with the 20 first places in the table of the Brazilian Soccer Championship
# considering the order of the positions. Then show:

# a: just the 1 first positions
# b: the last 4 positions of the table
# c: a list with the teams in alphabetical order
# d: in which position at the table is the team 'Juventude'

teams = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense',
 'Corinthians', 'Athletico-PR', 'Atlético-MG', 'América-MG',
  'Fortaleza', 'Botafogo', 'Santos', 'São Paulo', 'Bragantino',
   'Goiás', 'Coritiba', 'Ceará SC', 'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')
for t in teams:
    print(f'{t}\n')
print(f'first 5 in the ranking: {teams[:5]}\n') # vou considerar os 2 pontos como 'to end'
print(f'last 4 in the ranking: {teams[-4:]}\n') # pensar numa maneira de deixar td em colunas dps. .
print(f'In aphabetical order: {sorted(teams)}\n')
print(f'Juventude is in the {teams.index("Juventude")+1}° position') 
# qnd se usa o format, a aspa conflita com outra aspa, então basta usar aspas duplas 
# para q a interpolação seja compreendida. .
