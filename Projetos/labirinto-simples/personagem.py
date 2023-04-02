import pygame


class Char1():
    def __init__(self, tela):

        self.tela = tela

        # Cria o personagem que vai andar no labirinto!
        self.imagem = pygame.image.load(
            'Projetos\\labirinto-simples\\imagens\\char1.bmp')
        # transforma a imagem em um retângulo.
        self.rect = self.imagem.get_rect()

        # Deixar o personagem em algum canto da tela:
        

    def blitme(self):
        # Desenha o personagem na tela
        self.tela.blit(self.imagem, self.rect)
