import pygame
from settings import *
from player import Player
from overlay import Overlay

class Level:

    def __init__(self) -> None:
        
        #pegar a tela de superficie
        self.display_surface = pygame.display.get_surface()

        #sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        self.player = Player((640, 360), self.all_sprites) #posição e grupo do player

    def run(self, dt): #superficie que irá sempre atualizar
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface) #função draw dos sprites groups
        self.all_sprites.update(dt) #update method

        self.overlay.display()