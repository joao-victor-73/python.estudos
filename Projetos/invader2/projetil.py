import pygame
from pygame.sprite import Sprite


class Projetil(Sprite):
    # Uma classe que administra projéteis disparados pela espaçonave.

    def __init__(self, configs, tela, nave):
        # Cria um objeto para o projétil na posição autall da espaçonave.
        super(Projetil, self).__init__()

        self.tela = tela

        # ret_p é o retângulo do projetil
        # Cria um retângulo para o projétil em (0, 0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(
            0, 0, configs.projetil_largura, configs.projetil_altura)
        self.rect.centerx = nave.retangulo.centerx
        self.rect.top = nave.retangulo.top

        # Armazena a posição do projétil como um valor decimal:
        self.y = float(self.rect.y)
        self.cor = configs.projetil_cor
        self.velocidade = configs.projetil_velocidade

    def update(self):
        # Move o projétil para cima da tela.
        self.y -= self.velocidade

        # atualiza a posição de ret_p
        self.rect.y = self.y

    def desenha_projetil(self):
        # Desenha o projétil na tela.
        pygame.draw.rect(self.tela, self.cor, self.rect)
