import pygame
import sys
from level import *
from settings import *
from button import *

class Menu:
    def __init__(self):
        # Defina os elementos do menu, como botões e texto.
        self.start_button = Button("Start", (LARGURA_TELA // 2, 100))
        pass

    def draw(self, screen):
        screen.fill((255, 255, 255))  # Preencha a tela com uma cor de fundo
        self.start_button.draw(screen)
        pygame.display.update()
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                if self.start_button.is_clicked(event.pos):
                    self.start_button.is_hovered = True
                else:
                    self.start_button.is_hovered = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.is_clicked(event.pos):
                    print("Botão 'Start' clicado")
                    return "game"  # Retorne "game" quando o botão "Start" for clicado
        pass