import pygame

sound = "assets/Chill.wav"

def soundPlay ():
    pygame.mixer.init() 

    pygame.mixer.music.load(sound)
    pygame.mixer.music.set_volume(0.2)

    pygame.mixer.music.play(-1)
