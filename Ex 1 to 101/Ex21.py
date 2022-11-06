"""
Ex 21 - Make a python program that opens and plays audio from an mp3 file
"""
## if you are using the vs code remember to install a pip and install pygame module.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('iloveu.mp3')
pygame.mixer.music.play()

input('Can you hear it now? [enter to stop]')