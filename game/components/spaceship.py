import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP

class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    
    def __init__(self):
        self.image = SPACESHIP
        self.pygame = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)