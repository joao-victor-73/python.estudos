import pygame


class Char1():
    def __init__(self, tela):

        self.tela = tela

        # Cria o personagem que vai andar no labirinto! (por enquanto é um quadrado)
        self.char1 = pygame.draw.rect(tela, (250, 0, 0), (400, 300, 20, 20))