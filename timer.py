import pygame 

class Timer:
    def __init__(self, duration, func = None):
        self.durantion = duration
        self.func = func
        self.star_time = 0
        self.active = False
        
    def ativado(self):
        self.active = True
        self.star_time = pygame.time.get_ticks()
        
    def desativado(self):
        self.active = False
        self.star_time = 0
        
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.star_time >= self.durantion:
            self.desativado()
            if self.func:
                self.func()