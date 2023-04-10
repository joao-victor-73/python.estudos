class Configurações():
    def __init__(self):
        '''< Inicializa as configurações estáticas do jogo. >'''

        # Configurações da Tela:
        self.tela_largura = 1200  # width
        self.tela_altura = 800  # height
        self.fundo_tela = (230, 230, 230)

        # Configurações da espaçonave:
        self.nave_limite = 3

        # Configurações dos projéteis:
        self.projetil_largura = 3
        self.projetil_altura = 15
        self.projetil_cor = (60, 60, 60)
        self.projeteis_permitidos = 3

        # Configurações dos alienígenas:
        self.frota_velocidade = 10  # frota_velocidade = fleet_drop_speed
        ''' frota_velocidade também mexe com a velocidade de descer dos aliens'''

        # A taxa com que a velocidade do jogo aumenta
        self.aumentar_velocidade = 1.1  # speedup_scale

        # Taxa com que os pontos para cada alienígena aumentam
        self.score_scale = 1.5

        self.iniciar_configs_dinamicas()

    def iniciar_configs_dinamicas(self):
        '''< Inicializa as configurações que mudam no decorrer do jogo. >'''

        self.nave_velocidade = 1.5
        self.projetil_velocidade = 2
        self.alien_velocidade = 1   # alien_speed_factor
        self.frota_direcao = -1  # fleet_direction
        # frota_direção = a 1 representa a direita; = a -1 representa a esquerda

        self.pontos_alien = 25

    def incrementando_velocidade(self):
        '''< Aumenta as configurações de velocidade. >'''

        self.nave_velocidade *= self.aumentar_velocidade
        self.projetil_velocidade *= self.aumentar_velocidade
        self.alien_velocidade *= self.aumentar_velocidade

        self.pontos_alien = int(self.pontos_alien * self.score_scale)
        print(self.pontos_alien)
