import pygame
from settings import *

class Overlay:
    def __init__(self,player):

        # setup geral:
        self.display_surface = pygame.display.get_surface()
        self.player = player

        # imports:
        overlay_path = './graficos/overlay/'
        self.tools_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
        self.seeds_surf = {seed: pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}
        print(self.tools_surf)
        #print(self.seeds_surf)

    def display(self):

        # tools:
        tool_surf = self.tools_surf[self.player.ferramenta_selecionada]
        tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSICOES['tool'])
        self.display_surface.blit(tool_surf,tool_rect)

        # seeds:
        seed_surf = self.seeds_surf[self.player.sementes_selecionadas]
        seed_rect = seed_surf.get_rect(midbottom = OVERLAY_POSICOES['seed'])
        self.display_surface.blit(seed_surf, seed_rect)
