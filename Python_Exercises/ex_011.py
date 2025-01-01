#Make a program which reads the height and the lenght of a wall in meters. 
# Caculate it's area and the necessary quantity of paint to paint it. 
# Knowing that each liter of paint, paints an area of 2 square meters. .
lenght = float(input('What is the lenght of the wall? '))
height = float(input('What is the height of the wall? '))
sqm = height*lenght
tliter = sqm/2
print(f"Your wall has the dimension of {lenght} x {height} and it's area is: {sqm} square meters. .")
print(f"To paint this wall in it's totallity you would need {tliter} liters of paint.")
