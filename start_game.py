import pygame
from pygame.sprite import Sprite

# to make the start game button class
class Start_game(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # to load the image
        self.image = pygame.image.load('start_game1.png')
        self.rect = self.image.get_rect()

        # to make the start game initial possition
        self.rect.x = self.screen_rect.centerx-140
        self.rect.y = self.screen_rect.centery-80

    # to draw the image
    def blitme(self):
        self.screen.blit(self.image,self.rect)
