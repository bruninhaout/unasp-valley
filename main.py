import pygame
import sys
from settings import *
from level import *
from menu import *

pygame.display.set_caption('Unasp Valley')

class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.menu = Menu()
        self.current_screen = "menu"

    def run(self):
        current_screen = "menu"

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.current_screen == "menu":
                # Atualize e renderize o menu
                self.menu.draw(self.tela)
                menu_choice = self.menu.handle_events()
                if menu_choice == "game":
                    self.current_screen = "game"
            if self.current_screen == "game":
                dt = self.clock.tick() / 1000  # delta time
                self.level.run(dt)
                pygame.display.update()


if __name__ == '__main__':
    jogo = Game()
    jogo.run()
