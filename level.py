import pygame
from settings import *
from player import Player
from sprites import Generic

class Level:

    def __init__(self) -> None:
        
        #pegar a tela de superficie
        self.display_surface = pygame.display.get_surface()

        #sprite groups
        self.all_sprites = CameraGroup()

        self.setup()

    def setup(self):
        self.player = Player((640, 360), self.all_sprites) #posição e grupo do player
        Generic(
            pos = (0,0),
            surf = pygame.image.load('./graficos/world/ground.png').convert_alpha(),
            groups = self.all_sprites
        )

    def run(self, dt): #superficie que irá sempre atualizar
        self.display_surface.fill('black')
        self.all_sprites.custom_draw()
        self.all_sprites.update(dt) #update method

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def custom_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)