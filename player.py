import pygame
from settings import *
from suporte import *
from timer import Timer


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites, tree_sprites):
        super().__init__(group)

        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0
        
        #setup geral do player
        self.image = self.animations[self.status][self.frame_index] #criar o personagem com imagem
        self.rect = self.image.get_rect(center = pos) #posição (int)
        self.z = LAYERS['main']

        # setup geral do player
        # criar o personagem com imagem
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)  # posição (int)

        # atribuir movimentos
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        # timers
        self.timers = {
            'tool use': Timer(350, self.use_tool),
            'tool switch': Timer(200),
            'seed use': Timer(350, self.use_seed),
            'seed switch': Timer(200),

        }

        # tools
        self.tools = ['hoe', 'axe', 'water']
        self.tools_index = 0
        self.selected_tool = self.tools[self.tools_index]

        # seeds
        self.seeds = ['corn', 'tomato']
        self.seed_index = 0
        self.selected_seedss = self.seeds[self.seed_index]
        
        # interactions
        self.tree_sprites = tree_sprites
        

    def use_tool(self):
        
        if self.selected_tool == 'hoe':
            pass
        
        if self.selected_tool == 'axe':
            for tree in self.tree_sprites.sprites():
                if tree.rect.collidepoint(self.target_pos):
                    tree.damage()
        
        if self.selected_tool == 'water':
            pass

    def get_target_pos(self):
        self.target_pos = self.rect.center + PLAYER_TOOL_OFFSET[self.status.split('_')[0]]       
        
    def use_seed(self):
        pass
        #print(self.selected_seed)

    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                           'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
                           'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
                           'right_water': [], 'left_water': [], 'up_water': [], 'down_water': []}

        for animation in self.animations.keys():
            full_path = 'graficos/character/' + animation
            self.animations[animation] = import_folder(full_path)
        print(self.animations)

    def animate(self, dt):
        # pick the number of imagens (0, 1, 2, 3..) de acordo com o que esta na pasta
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):  # função para controlar o player
        teclas = pygame.key.get_pressed()

        if not self.timers['tool use'].active:
            # direções
            if teclas[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif teclas[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if teclas[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            elif teclas[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            # uso ferramenta
            if teclas[pygame.K_SPACE]:
                # time para o uso da ferramenta
                self.timers['tool use'].ativado()
                self.direction = pygame.math.Vector2()

            # troca de ferramenta
            if teclas[pygame.K_f] and not self.timers['tool switch'].active:
                self.timers['tool switch'].ativado()
                self.tools_index += 1
                # se tool index > quantidade de ferramentas o index volta pra 0
                self.tools_index = self.tools_index if self.tools_index < len(
                    self.tools) else 0

                self.selected_tool = self.tools[self.tools_index]

            # uso das sementes
            if teclas[pygame.K_LCTRL]:
                # time para o uso da ferramenta
                self.timers['seed use'].ativado()
                self.direction = pygame.math.Vector2()
                print('use seed')

            # troca das sementes
            if teclas[pygame.K_e] and not self.timers['seed switch'].active:
                self.timers['seed switch'].ativado()
                self.seed_index += 1
                # se tool index > quantidade de ferramentas o index volta pra 0
                self.seed_index = self.seed_index if self.seed_index < len(self.seeds) else 0
                self.selected_seedss = self.seeds[self.seed_index]
                print(self.selected_seedss)

    def get_status(self):  # verificar se esta parado
        # se o player esta se movendo add _idle
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'

        # uso da ferramenta
        if self.timers['tool use'].active:
            self.status = self.status.split(
                '_')[0] + '_' + self.selected_tool

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def movimento(self, dt):

        # normalizando movimento do vetor (manter a direção/velocidade em 1 na diagonal
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # movimento horizontal (importante para colisão)
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # movimento vertical (importante para colisão)
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.get_target_pos()
        
        self.movimento(dt)
        self.animate(dt)