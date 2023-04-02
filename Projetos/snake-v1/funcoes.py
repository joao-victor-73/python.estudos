import pygame
import mensagem as msg
import sys
from configs import Configurações


def reiniciar():
    ''' Função que server para o jogo voltar para o inicio, um reinicio. '''
    import random
    config = Configurações()

    global pontos, velocidade, cont, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x2, y2, morreu

    config.pontos = config.cont = 0
    config.velocidade = 10
    config.comprimento_inicial = 5

    x_cobra = ((config.tela_largura/2) - (80 / 2))
    y_cobra = ((config.tela_altura/2) - (60 / 2))

    lista_cabeca = []
    lista_cobra = []

    x2 = random.randint(40, 600)
    y2 = random.randint(50, 430)

    morreu = False


def encostou_borda(x_cobra, y_cobra, config, cor, tela):
    ''' Essa função vai verificar se foi encontado nas bordas ou não '''

    if (x_cobra > config.tela_largura or x_cobra < 0) or (y_cobra < 0 or y_cobra > config.tela_altura):
        men_over, texto_retangulo = msg.mensagem_game_over()

        morreu = True

        while morreu:
            tela.fill(cor.cinza_claro)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        reiniciar()

            texto_retangulo.center = (
                config.tela_largura // 2, config.tela_altura // 2)

            tela.blit(men_over, texto_retangulo)
            pygame.display.update()


def encostou_na_cabeca(lista_cobra, lista_cabeca, config, cor, tela):
    ''' Caso o jogador encoste no corpo da cobra, o jogador vai perder! '''
    if lista_cobra.count(lista_cabeca) > 1:
        men_over, texto_retangulo = msg.mensagem_game_over()

        morreu = True

        while morreu:
            tela.fill(cor.cinza_claro)
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
