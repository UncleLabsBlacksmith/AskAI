import pygame

def playsound():

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('test.wav')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

playsound()