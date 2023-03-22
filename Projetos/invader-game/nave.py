import pygame


class Nave():
    def __init__(self, config, tela):
        self.tela = tela
        self.config = config  # config == ai_settings

        # Carregar a imagem da espaçonave e obtém seu rect
        self.imagem = pygame.image.load(
            'Projetos\\invader-game\\imagens\\nave_galata.bmp')
        self.imagem = pygame.transform.scale(self.imagem, [80, 80])
        # comando para redimensionar tamanho da imagem
        self.rect = self.imagem.get_rect()
        self.tela_rect = tela.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.tela_rect.centerx
        self.rect.bottom = self.tela_rect.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)

        # Flag de movimento
        self.movendo_direita = False
        self.movendo_esquerda = False

    def atualizar(self):
        # Atualiza a posição da espaçonave de acordo com a flag de movimento.

        # Atualiza o valor do centro da espaçonave, e não o retângulo
        if self.movendo_direita:
            self.center += self.config.fator_velocidade_nave

        if self.movendo_esquerda:
            self.center -= self.config.fator_velocidade_nave

        # Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center

    def blitme(self):
        self.tela.blit(self.imagem, self.rect)
