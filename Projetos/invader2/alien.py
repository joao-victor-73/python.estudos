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

    def blitme(self):
        # Desenha o alienígena em sua posição atual.
        self.tela.blit(self.image, self.rect)
