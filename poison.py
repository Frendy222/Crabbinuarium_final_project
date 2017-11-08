import pygame
from pygame.sprite import Sprite
import random

# make the poison class
class Poison(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # make the image
        self.image = pygame.image.load('poison.png')
        self.rect = self.image.get_rect()

        # to make it appear randomly
        xcor = random.randint(30,500)

        # position
        self.rect.x = xcor
        self.rect.y = 0

    # to draw the image
    def blitme(self):
        self.screen.blit(self.image,self.rect)
