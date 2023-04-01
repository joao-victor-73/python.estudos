import pygame
import sys
from pygame.sprite import Sprite, Group

pygame.init()


class Dino(Sprite):
    def __init__(self):
        super(Sprite).__init__()

        self.sprites = []

        self.sprites.append(pygame.image.load(
            'Projetos\\aula12 - sprites\\walk\\Walk (1).png'))
        self.sprites.append(pygame.image.load(
            'Projetos\\aula12 - sprites\\walk\\Walk (2).png'))
        self.sprites.append(pygame.image.load(
            'Projetos\\aula12 - sprites\\walk\\Walk (3).png'))
        self.sprites.append(pygame.image.load(
            'Projetos\\aula12 - sprites\\walk\\Walk (4).png'))
        self.sprites.append(pygame.image.load(
            'Projetos\\aula12 - sprites\\walk\\Walk (5).png'))
        self.sprites.append(pygame.image.load(
            'Projetos\\aula12 - sprites\\walk\\Walk (6).png'))
        self.sprites.append(pygame.image.load(
            'Projetos\\aula12 - sprites\\walk\\Walk (7).png'))
        self.sprites.append(pygame.image.load(
            'Projetos\\aula12 - sprites\\walk\\Walk (8).png'))
        self.sprites.append(pygame.image.load(
            'Projetos\\aula12 - sprites\\walk\\Walk (9).png'))
        self.sprites.append(pygame.image.load(
            'Projetos\\aula12 - sprites\\walk\\Walk (10).png'))

        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100


largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('TESTANDO SPRITES!')

todas_as_sprites = Group()
dino = Dino()
todas_as_sprites.add(dino)


while True:
    tela.fill(0, 0, 0)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()
