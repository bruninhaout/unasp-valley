from pygame.math import Vector2
#tela
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_SIZE = 64

#POSICOES 
OVERLAY_POSITIONS = {
	'tool' : (80, SCREEN_HEIGHT - 40),
	'seed' : (140, SCREEN_HEIGHT - 20)}

PLAYER_TOOL_OFFSET = {
	'left': Vector2(-50,40),
	'right': Vector2(50,40),
	'up': Vector2(0,-10),
	'down': Vector2(0,50)
}

LAYERS = {
	'water': 0,
	'ground': 1,
	'soil': 2,
	'soil water': 3,
	'rain floor': 4,
	'house bottom': 5,
	'ground plant': 6,
	'main': 7,
	'house top': 8,
	'fruit': 9,
	'rain drops': 10
}

APPLE_POS = {
	'Small': [(18,17), (30,37), (12,50), (30,45), (20,30), (30,10)],
	'Large': [(30,24), (60,65), (50,50), (16,40),(45,50), (42,70)]
}

GROW_SPEED = {
	'Milho': 1,
	'Tomate': 0.7
}

SALE_PRICES = {
	'Madeira': 4,
	'Maça': 2,
	'Milho': 10,
	'Tomate': 20
}
PURCHASE_PRICES = {
	'Semente de Milho': 5,
	'Semente de Tomate': 5
}