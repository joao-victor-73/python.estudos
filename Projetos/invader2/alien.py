import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # Classe que representa um único aienígena.

    def __init__(self, configs, tela):
        # inicializa o alienígina e define sua posição incial;
        super(Alien, self).__init__()

        self.tela = tela
        self.configs = configs

        # Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load(
            'Projetos\\invader2\\imagens\\alien-nave_1.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada novo alienígina próximo à parte superior esquerda da tela.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)

    def checando_borda(self):  # check_edges
        ''' Devolve True se o alienígena estiver na borda da tela. '''
        tela_rect = self.tela.get_rect()

        if self.rect.right >= tela_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        ''' Move o alienígena para a direita ou para a esquerda. '''
        self.x += (self.configs.alien_velocidade * self.configs.frota_direcao)
        self.rect.x = self.x

    def blitme(self):
        # Desenha o alienígena em sua posição atual.
        self.tela.blit(self.image, self.rect)
