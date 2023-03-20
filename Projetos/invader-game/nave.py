import pygame


class Nave():
    def __init__(self, tela):
        self.tela = tela

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

        # Flag de movimento
        self.movendo_direita = False
        self.movendo_esquerda = False

    def atualizar(self):
        # Atualiza a posição da espaçonave de acordo com a flag de movimento.
        if self.movendo_direita:
            self.rect.centerx += 1
        
        if self.movendo_esquerda:
            self.rect.centerx -= 1

    def blitme(self):
        self.tela.blit(self.imagem, self.rect)
