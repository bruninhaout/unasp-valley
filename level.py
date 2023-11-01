import pygame
from settings import *
from player import Player
from sprites import Generic, Water, WildFlower, Tree
from overlay import Overlay
from pytmx.util_pygame import load_pygame
from suporte import *

class Level:

    def __init__(self) -> None:
        
        #pegar a tela de superficie
        self.display_surface = pygame.display.get_surface()

        #sprite groups
        self.all_sprites = CameraGroup()

        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        tmx_data = load_pygame('./data/map.tmx')
        
        # house floor and carpets
        for layer in ['HouseFloor', 'HouseFurnitureBottom']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE,y * TILE_SIZE), surf, self.all_sprites, LAYERS['house bottom'])
        # house walls and furniture
        for layer in ['HouseWalls', 'HouseFurnitureTop']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE,y * TILE_SIZE), surf, self.all_sprites)

		# Fence
        for x, y, surf in tmx_data.get_layer_by_name('Fence').tiles():
            Generic((x * TILE_SIZE,y * TILE_SIZE), surf, self.all_sprites)

		# water 
        water_frames = import_folder ('./graficos/water')
        for x, y, surf in tmx_data.get_layer_by_name('Water').tiles():
            Water((x * TILE_SIZE,y * TILE_SIZE), water_frames, self.all_sprites)

		# trees
        for obj in tmx_data.get_layer_by_name('Trees'):
            Tree((obj.x, obj.y), obj.image, self.all_sprites, obj.name)

		# wildflowers 
        for obj in tmx_data.get_layer_by_name('Decoration'):
            WildFlower((obj.x, obj.y), obj.image, self.all_sprites)
        
        self.player = Player((640, 360), self.all_sprites) #posição e grupo do player
        Generic(
            pos = (0,0),
            surf = pygame.image.load('./graficos/world/ground.png').convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['ground']
        )

def player_add(self, item):

    self.player.item_invertory[item] += 1


    def run(self, dt): #superficie que irá sempre atualizar
        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt) #update method
        self.overlay.display()

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - LARGURA_TELA / 2
        self.offset.y = player.rect.centery - ALTURA_TELA  / 2
        
        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
        