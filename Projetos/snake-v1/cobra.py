import pygame


class Cobra():
    def __init__(self, config, tela, cor,):
        ''' Essa será a classe que coordenará todo o código do personagem cobra. '''

        self.x_cobra = ((config.tela_largura/2) - (80 / 2))
        self.y_cobra = ((config.tela_altura/2) - (60 / 2))
        # em x e y foi feito um calcúlo p/
        # deixar o objeto no meio da tela

        # largura_tela / 2 - 80 / 2 -> 80 é a largura do objeto que vai ficar no meio!

        self.cobra = pygame.draw.rect(tela, cor.verde, (self.x_cobra, self.y_cobra, 20, 20))

        


