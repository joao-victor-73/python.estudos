class Configurações():
    def __init__(self):
        # Configurações da Tela:
        self.tela_largura = 1200  # width
        self.tela_altura = 800  # height
        self.fundo_tela = (230, 230, 230)

        # Configurações da espaçonave:
        self.nave_velocidade = 1.5
        self.nave_limite = 3

        # Configurações dos projéteis:
        self.projetil_velocidade = 2
        self.projetil_largura = 3
        self.projetil_altura = 15
        self.projetil_cor = (60, 60, 60)
        self.projeteis_permitidos = 3

        # Configurações dos alienígenas:
        self.alien_velocidade = 1   # alien_velocidade = alien_speed_factor
        self.frota_velocidade = 20  # frota_velocidade = fleet_drop_speed
        ''' frota_velocidade também mexe com a velocidade de descer '''

        self.frota_direcao = -1  # fleet_direction
        # frota_direção = a 1 representa a direita; = a -1 representa a esquerda
