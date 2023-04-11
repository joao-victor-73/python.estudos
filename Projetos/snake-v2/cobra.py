import pygame


class Cobra():
    def __init__(self, configs, tela):
        self.tela = tela
        self.configs = configs

        # Configurações da cobra:
        self.posicao_x = (configs.tela_largura/2)
        self.posicao_y = (configs.tela_altura/2)

        self.corpo = [20, 20]  # Tamanho de cada pixel da cobra

        # Flags de Movimentação:
        self.cima = False
        self.baixo = False
        self.esquerda = False
        self.direita = False

    def desenha_cobra(self):
        '''< Desenha a cobra quando essa função for chamada. >'''
        pygame.draw.rect(self.tela, (0, 255, 0), (self.posicao_x,
                         self.posicao_y, self.corpo[0], self.corpo[1]))
