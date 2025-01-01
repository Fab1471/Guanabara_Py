# Write a program that reads the speed of a car.
# If it exceeds 80km/h, show a message saying he was fined.
# The traffic ticket will cost R$7 per each km/h above the limit.

speed = float(input("What's the current speed of the car? "))
trafficvalue = (speed -80) * 7
if speed >80:
    print('You exceeded the maximum allowed limit!')
    print("You're gonna receive a traffic ticket due to your infraction.")
    print(f'The value you ought to pay is: {trafficvalue:.2f}')
print('Drive safely. Have a nice day.')
