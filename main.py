import pygame, sys
from settings import *
from level import *
from menu import *

class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Unasp-Vallew")
        self.clock = pygame.time.Clock()
        #self.menu = Menu()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 1000 #delta time
            self.level.run(dt)
            pygame.display.update()

if __name__ == '__main__':
    jogo = Game()
    jogo.run()

