import pygame
from settings import *
from settings import LAYERS
from random import randint, choice
from timer import Timer

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
        
class Water(Generic):
	def __init__(self, pos, frames, groups):

		#animation setup
		self.frames = frames
		self.frame_index = 0

		# sprite setup
		super().__init__(
				pos = pos, 
				surf = self.frames[self.frame_index], 
				groups = groups, 
				z = LAYERS['water']) 

	def animate(self,dt):
		self.frame_index += 5 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,dt):
		self.animate(dt) 

class WildFlower(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)

class Tree(Generic):
    def __init__(self, pos, surf, groups, name):
        super().__init__(pos, surf, groups)
        
        #tree atributes
        self.health = 5
        self.alive = True
        stump_path = f'./graficos/stumps/{"small" if name == "Small" else "large"}.png'
        self.stump_surf = pygame.image.load(stump_path).convert_alpha()
        self.invul_timer = Timer(200)
        
        #maças
        self.apples_surf = pygame.image.load('./graficos/fruit/apple.png')
        self.apple_pos - APPLE_POS[name]
        self.apple_sprites = pygame.sprite.Group()
        
    def damege(self):
        #damaging the tree
        self.health -= 1
        
        #remove the apple
        if len(self.apple_sprites()) > 0:
            random_apple = choice(self.apple_sprites())
            random_apple.kill()
            
    def check_death(self):
        if self.health <= 0:
            self.image = self.stump_surf
            self.rect = self.image.get.rect(midbottom = self.rect.midbottom)
            self.hitbox = self.rect.copy().inflate(-10, -self.rect.height * 0.6) 
            self.alive = False
            
    def update(self, dt):
        if self.alive:
            self.check_death()
         
    def create_fruit(self):
        for pos in self.apples_pos:
            if randint(0, 10) < 2:
                x = pos[0] + self.rect.left
                y = pos[1] + self.rect.top
                Generic(
                	pos = (x, y), 
                	surf = self.apples_surf, 
                	groups = [self.apple_sprites, self.groups()[0]], 
                	z = LAYERS['fruit'])
                
                