import pygame
from random import randint


class Comida():
    def __init__(self, config, tela, cor):
        self.config = config
        self.tela = tela
        self.cor = cor

        # Se o tamanho da tela mudar, mudar também essas variáveis
        self.maca_x = randint(40, 600)
        self.maca_y = randint(50, 430)

        self.tamanho_comida = [10, 10]

    def desenhar_maca(self):
        '''< Desenha a comida. >'''
        return pygame.draw.rect(self.tela, self.cor.azul, (self.maca_x, self.maca_y, self.tamanho_comida[0], self.tamanho_comida[1]))
