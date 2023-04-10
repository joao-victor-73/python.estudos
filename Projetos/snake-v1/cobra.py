import pygame

class Cobra():
    def __init__(self, config, tela, cor):
        self.config = config
        self.tela = tela
        self.cor = cor

        self.lista_cobra = [] # lista que vai servir para guardar os aumentos da cobra!
        self.lista_cabeca = []


    def aumenta_cobra(self):
        for XeY in self.lista_cobra:
            # XeY vai ser igual a uma lista [].
            # XeY[0] = x
            # XeY[1] = y
            pygame.draw.rect(self.tela, self.cor.verde, (XeY[0], XeY[1], 20, 20))

    def 
