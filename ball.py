import pygame
import random
from mixer import *

# class definition
class Ball:

    # constructor 
    def __init__(self, screen): 
        self.x = 0
        self.y = 0
        self.r = 20
        self.power = 25
        self.speed = self.power
        self.moveDirection = 1 if random.uniform(0,1) > 0.5  else -1
        self.xMoveStep = 20
        self.color = [ random.randint(50,250), random.randint(0,250), random.randint(0,250) ]
        self.width = screen.get_width()
        self.sound = loadSound()

    # method 
    def draw(self, screen):
        self.bounce(screen)
        pygame.draw.circle(
           screen,  # Surface to draw on
            [255,255,255],  # Color in RGB Fashion
            [self.x, self.y],  # Center
            self.r,  # Radius
        )
        pygame.draw.circle(
           screen,  # Surface to draw on
            self.color,  # Color in RGB Fashion
            [self.x, self.y],  # Center
            self.r-0.5,  # Radius
        )
        
    def setRadius(self, r ):
        self.r = r

    def setPower(self, power) :
        self.power = power
        self.speed = power

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def bounce(self,screen):
        width = screen.get_width()
        if self.y > 800:
            self.speed = self.power
            self.sound.play()
        self.y -= self.speed
        self.speed -= 0.5
        if self.x < self.r or self.x > width -self.r*1.2:
            self.moveDirection *= -1
        
        self.x += random.randint(0, self.xMoveStep) * self.moveDirection  

