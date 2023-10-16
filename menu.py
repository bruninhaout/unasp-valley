import pygame
import sys
from level import *
from settings import *
from button import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('graficos/menu/Nintendo Wii - Shop Channel Music (Extended) HQ.mp3')

back = pygame.image.load('graficos/menu/i295429.jpeg')
image = pygame.transform.scale(back, (LARGURA_TELA, ALTURA_TELA))

class Menu:
    pygame.mixer.music.play(loops=99, start=0.0)
    def __init__(self):
        # Defina os elementos do menu, como botões e texto.
        self.start_button = Button("COMEÇAR!", (LARGURA_TELA // 2.7, 250))
        self.exit_button = Button("SAIR", (LARGURA_TELA // 2.7, 400))

    def draw(self, screen):
        screen.blit(image, (0, 0))  # Preencha a tela com uma cor de fundo
        self.start_button.draw(screen)
        self.exit_button.draw(screen)
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
                if self.exit_button.is_clicked(event.pos):
                    self.exit_button.is_hovered = True
                else:
                    self.exit_button.is_hovered = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.is_clicked(event.pos):
                    print("Botão 'Start' clicado")
                    return "game"  # Retorne "game" quando o botão "Start" for clicado

                elif self.exit_button.is_clicked(event.pos):
                    print("Botão 'Sair' clicado")
                    pygame.quit()
                    sys.exit()
        pass
