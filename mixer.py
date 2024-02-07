#import pygame
import pygame.mixer

def loadBGM():
    pygame.mixer.init() 
    pygame.mixer.music.load("assets/Chill.wav")
    pygame.mixer.music.set_volume(0.5)

def loadSound():
    sound = pygame.mixer.Sound("assets/Coin.wav")
    sound.set_volume(0.2)
    return sound


def musicPlay ():
    pygame.mixer.music.play(-1)

