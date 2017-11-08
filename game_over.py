import pygame
from pygame.sprite import Sprite

# to make the game over class
class Game_over(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('game_over.png')
        self.rect = self.image.get_rect()


        self.rect.x = self.screen_rect.centerx-140
        self.rect.y = self.screen_rect.centery-80

    # to draw the img later
    def blitme(self):
        self.screen.blit(self.image,self.rect)
