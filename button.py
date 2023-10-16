import pygame

pygame.init()
pygame.mixer.init()

efeito_sonoro = pygame.mixer.Sound('graficos/menu/minecraft-hurt_kg1jeLX.mp3')

class Button:
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.font = pygame.font.Font(None, 40)
        self.width = 350
        self.height = 100
        self.width2 = 375
        self.height2 = 125
        self.rect = pygame.Rect(pos[0], pos[1], self.width, self.height)
        self.rect2 = pygame.Rect(pos[0], pos[1], self.width2, self.height2, )
        self.color = (0, 128, 255)
        self.hover_color = (0, 200, 255)
        self.text_color = (255, 255, 255)
        self.is_hovered = False
        self.original_rect = self.rect.copy()

    hovered = False

    def draw(self, screen):

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.hover_color, self.rect2)
            efeito_sonoro.play()
            hovered = True

        else:
            pygame.draw.rect(screen, self.color, self.rect)
            hovered = False

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
