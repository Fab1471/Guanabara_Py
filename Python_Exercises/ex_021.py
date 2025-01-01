# Make a program in Python that opens and plays the audio of a mp3 archive. .

'''import pygame
pygame.init()
pygame.mixer.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

from playsound import playsound
playsound('/home/fabri/projects/Python_Exercises/ex_021.mp3')
