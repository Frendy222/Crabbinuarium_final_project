import pygame
from pygame.sprite import Sprite
import random

# make the food class
class Food(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # to load the food image
        self.image = pygame.image.load('crab_sushi.png')
        self.rect = self.image.get_rect()

        # to make the food appear randomly
        xcor = random.randint(30,500)

        self.rect.x = xcor
        self.rect.y = 0

    # to draw the food
    def blitme(self):
        self.screen.blit(self.image,self.rect)
