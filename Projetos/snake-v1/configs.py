import pygame


class Configurações():

    # Configurações da Tela e coisas Iniciais
    def __init__(self):
        self.tela_largura = 640
        self.tela_altura = 480
        self.tela_cor = (80, 60, 60)  # Cor de Fundo da Tela

        # Variável que vai dizer que tamanho a cobra estará ao iniciar
        self.comprimento_inicial = 5

        self.pontos = 0  # variável para armazenar a pontuação
        self.cont = 0  # Variável contador para tocar música de 10 pontos

        self.velocidade = 10  # variável para velocidade do objeto


    # Configurações de Fontes
'''
    def fontes(self, fonte='arial', tamanho='15', negrito=False, italico=False):
        # Fonte = o tipo de fonte que vai querer;
        # tamanho = O tamanho da Fonte (valores inteiros);
        # Negrito = Colocar True para colocar em negrito
        # Italico = Colocar True para colocar em Italico

        pygame.font.SysFont(fonte, tamanho, negrito, italico)
'''


# Configurações de Música
class Musicas():

    def __init__(self):
        pygame.init()
        pygame.mixer.music.set_volume(0.25)  # controla volume da músicas

        # Criando uma variável para que ela receba a música de fundo
        self.musica_background = pygame.mixer.music.load(
            'Projetos\\snake-v1\\sons\\CPU Talk.mp3')
        pygame.mixer.music.play(-1)
        # vai fazer a musica tocar, e o parâmetro -1 vai servir para tocar ela novamente assim que terminar

        # Música para quando houver colisão
        self.musica_coleta = pygame.mixer.Sound(
            'Projetos\\snake-v1\\sons\\smw_coin.wav')

        # Vai fazer um barulho toda vez que juntar 10 pontos
        self.musica_10pontos = pygame.mixer.Sound(
            'Projetos\\snake-v1\\sons\\smw_dragon_coin.wav')


class Cores():

    def __init__(self):
        self.vermelho = (255, 0, 0)
        self.verde = (0, 255, 0)
        self.azul = (0, 0, 255)
