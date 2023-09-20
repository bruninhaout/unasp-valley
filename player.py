import pygame
from pygame.sprite import _Group
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group) -> None:
        super().__init__(group)
        self.image = pygame.Surface((64, 32))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)
        