# Create a program that reads the name of a city and tells whether
# it starts or not with the name "Santo"

city = str(input("What's the name of the city? ")).strip() # stripou para eliminar espaços inuteis
print(city[:5].upper() == 'SANTO') # tacou tudo pra maiscula 
