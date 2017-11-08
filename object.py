# to import the pygame and random to get the function in it

import pygame
from pygame.sprite import Sprite

# make the class crab
class Crab(Sprite):
    def __init__(self,screen):
        Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # to load the image and resize it
        self.crab = pygame.image.load('crab_big.png')

        # comppoint is the compresstion point or to how much it need to be compressed
        self.comppoint = 0.02
        self.crab_rect = self.crab.get_rect()
        self.crab_x = self.crab_rect.width
        self.crab_y = self.crab_rect.height
        self.image = pygame.transform.scale(self.crab,(int(self.crab_x*self.comppoint),int(self.crab_y*self.comppoint)))
        self.rect = self.image.get_rect()

        # to make the crab initial possition
        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = 378


        self.x = float(self.rect.centerx)
        self.y = float(self.rect.y)

    # to draw the crab
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    # to make the crab grow
    def growth(self):
        self.comppoint += 0.001
        self.rect.y -= 3
        self.image = pygame.transform.scale(self.crab,(int(self.crab_x*self.comppoint),int(self.crab_y*self.comppoint)))

    # to make the crab size back to small size
    def reset(self):
        self.comppoint = 0.02
        self.rect.y = 378
        self.image = pygame.transform.scale(self.crab,(int(self.crab_x*self.comppoint),int(self.crab_y*self.comppoint)))

