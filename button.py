import pygame

class Button:
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.font = pygame.font.Font(None, 36)
        self.width = 200
        self.height = 50
        self.rect = pygame.Rect(pos[0], pos[1], self.width, self.height)
        self.color = (0, 128, 255)
        self.hover_color = (0, 200, 255)
        self.text_color = (255, 255, 255)
        self.is_hovered = False

    def draw(self, screen):
        if self.is_hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)