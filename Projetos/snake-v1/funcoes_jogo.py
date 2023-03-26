import pygame
import sys
from random import randint
from configs import Configurações

config = Configurações()


def reiniciar():
    global pontos, velocidade, cont, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x2, y2, morreu

    config.pontos = config.cont = 0
    config.velocidade = 10
    config.comprimento_inicial = 5

    x_cobra = ((config.tela_largura/2) - (80 / 2))
    y_cobra = ((config.tela_altura/2) - (60 / 2))

    lista_cabeca = []
    lista_cobra = []

    x2 = randint(40, 600)
    y2 = randint(50, 430)

    morreu = False


def game_over(tela):
    import mensagem as mensagem

    men_over, texto_retangulo = mensagem.mensagem_game_over()

    morreu = True

    while morreu:
        tela.fill((176, 196, 222))
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    reiniciar()

        texto_retangulo.center = (config.tela_largura // 2,
                                    config.tela_altura // 2)

        tela.blit(men_over, texto_retangulo)
        pygame.display.update()