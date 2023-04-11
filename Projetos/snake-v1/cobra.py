import pygame


class Cobra():
    def __init__(self, config, tela, cor):
        self.config = config
        self.tela = tela
        self.cor = cor

        self.x_cobra = ((config.tela_largura/2) - (80 / 2))
        self.y_cobra = ((config.tela_altura/2) - (60 / 2))
        self.corpo = [20, 20]  # Tamanho do pixel da cobra

        # Movimentações
        self.x_controle = config.velocidade
        self.y_controle = 0

    def desenhar_cobra(self):
        '''< Desenha a cobra quando essa função for chamada. >'''
        return pygame.draw.rect(self.tela, self.cor.verde, (self.x_cobra, self.y_cobra, self.corpo[0], self.corpo[1]))
