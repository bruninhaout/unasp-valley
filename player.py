import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group) -> None:
        super().__init__(group)

        #setup geral do player
        self.image = pygame.Surface((32, 64)) #tamanho 
        self.image.fill('green') #cor
        self.rect = self.image.get_rect(center = pos) #posição (int)

        #atribuir movimentos
        self.direcao = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def input(self): #função para controlar o player
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_UP]:
            self.direcao.y = -1
        elif teclas[pygame.K_DOWN]:
            self.direcao.y = 1
        else:
            self.direcao.y = 0

        if teclas[pygame.K_RIGHT]:
            self.direcao.x = 1
        elif teclas[pygame.K_LEFT]:
            self.direcao.x = -1
        else:
            self.direcao.x = 0

    def movimento(self, dt):
        self.pos += self.direcao * self.speed * dt
        self.rect.center = self.pos

    def update(self, dt):
        self.input()
        self.movimento(dt)