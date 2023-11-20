import pygame
from settings import *
from suporte import import_folder
from sprites import Generic
from random import randint, choice
from math import isclose


class Sky:
    def __init__(self):
        self.flag = 0
        self.display_surface = pygame.display.get_surface()
        self.full_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.start_color = [255,255,255]
        self.start_reset = [255,255,255]
        self.end_color = (38,101,189)

    def display(self, dt):
        for index, value in enumerate(self.end_color):
            if self.start_color[index] > value and self.flag == 0:
                self.start_color[index] -= 2 * dt

            if isclose(self.start_color[index], 38, rel_tol=1e-1):
                self.flag = 1

        for index_day, value in enumerate(self.start_reset):
            if self.start_color[index_day] < value and self.flag == 1:
                print(self.start_color[index_day])
                self.start_color[index_day] += 2 * dt

            if isclose(self.start_color[0], 255, rel_tol=1e-1):
                self.flag = 0

        self.full_surf.fill(self.start_color)
        self.display_surface.blit(self.full_surf, (0,0), special_flags = pygame.BLEND_RGBA_MULT)


class Drop(Generic):
    def __init__(self, surf, pos, moving, groups, z):
        
        #general setup
        super().__init__(pos, surf, groups, z)
        self.lifetime = randint(400,500)
        self.start_time = pygame.time.get_ticks()
        
		# moving 
        self.moving = moving
        if self.moving:
            self.pos = pygame.math.Vector2(self.rect.topleft)
            self.direction = pygame.math.Vector2(-2,4)
            self.speed = randint(200,250)

    def update(self,dt):
		# movement
        if self.moving:
            self.pos += self.direction * self.speed * dt
            self.rect.topleft = (round(self.pos.x), round(self.pos.y))

		# timer
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()


class Rain:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.rain_drops = import_folder('./graficos/rain/drops')
        self.rain_floor = import_folder('./graficos/rain/floor')
        self.floor_w, self.floor_h = pygame.image.load('./graficos/world/ground.png').get_size()

    def create_floor(self):
        Drop(
			surf = choice(self.rain_floor), 
			pos = (randint(0,self.floor_w),randint(0,self.floor_h)), 
			moving = False, 
			groups = self.all_sprites, 
			z = LAYERS['rain floor'])

    def create_drops(self):
        Drop(
			surf = choice(self.rain_drops), 
			pos = (randint(0,self.floor_w),randint(0,self.floor_h)), 
			moving = True, 
			groups = self.all_sprites, 
			z = LAYERS['rain drops'])

    def update(self):
        self.create_floor()
        self.create_drops()
