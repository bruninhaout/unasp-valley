import pygame
from settings import *
from suporte import *
from timer import Timer

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()
        self.status = 'down_idle' 
        self.frame_index = 0
        
        #setup geral do player
        self.image = self.animations[self.status][self.frame_index] #criar o personagem com imagem
        self.rect = self.image.get_rect(center = pos) #posição (int)
        self.z = LAYERS['main']

        #atribuir movimentos
        self.direcao = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
        #timers
        self.timers = {
            'tool use': Timer(350, self.use_tool)
        }
        
        #tools
        self.ferramenta_selecionada = 'axe'
    def use_tool(self):
        print(self.ferramenta_selecionada)
        
    def import_assets(self):
        self.animations = {'up': [],'down': [],'left': [],'right': [],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
						   'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
						   'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
						   'right_water':[],'left_water':[],'up_water':[],'down_water':[]}

        for animation in self.animations.keys():
            full_path = 'graficos/character/' + animation
            self.animations[animation] = import_folder(full_path)
        print(self.animations)

    def animate (self, dt):
        self.frame_index += 4 * dt #pick the number of imagens (0, 1, 2, 3..) de acordo com o que esta na pasta
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations [self.status][int(self.frame_index)]
        
    def input(self): #função para controlar o player
        teclas = pygame.key.get_pressed()
        
        if not self.timers['tool use'].active:
            #direções
            if teclas[pygame.K_UP]:
                self.direcao.y = -1
                self.status = 'up'
            elif teclas[pygame.K_DOWN]:
                self.direcao.y = 1
                self.status = 'down'
            else:
                self.direcao.y = 0

            if teclas[pygame.K_RIGHT]:
                self.direcao.x = 1
                self.status = 'right'
            elif teclas[pygame.K_LEFT]:
                self.direcao.x = -1
                self.status = 'left'
            else:
                self.direcao.x = 0
                
            #uso ferramenta
            if teclas[pygame.K_SPACE]:
                #time para o uso da ferramenta
                self.timers['tool use'].ativado()
                self.direcao = pygame.math.Vector2()
            

    def get_status(self): #verificar se esta parado
        #se o player esta se movendo add _idle 
        if self.direcao.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
            
        #uso da ferramenta
        if self.timers['tool use'].active:
            self.status = self.status.split('_')[0] + '_' + self.ferramenta_selecionada
    
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()
    
    def movimento(self, dt):

        #normalizando movimento do vetor (manter a direção/velocidade em 1 na diagonal
        if self.direcao.magnitude() > 0: 
            self.direcao = self.direcao.normalize()

        #movimento horizontal (importante para colisão)
        self.pos.x += self.direcao.x * self.speed * dt
        self.rect.centerx = self.pos.x

        #movimento vertical (importante para colisão)
        self.pos.y += self.direcao.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.movimento(dt)
        self.animate(dt)