import pygame
import sys

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGO LABIRINTO')


while True:
    tela.fill((0, 0, 0))

    pygame.draw.rect(tela, (250, 0, 0), (400, 300, 20, 20))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
