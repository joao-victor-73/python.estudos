import pygame
import sys
import random

'''Sistema de pontuações, pode ser criado adicionando uma lista e quando o
jogo for encerrado, as pontuações são armazenadas em uma lista ou dicionário'''

'''Tela de jogo de menu que o jogador vai botar seu nome para pontuação e dentro
do menu vai ter opção de JOGAR e SOBRE.'''

''' JOGO com problema na hora de pegar a maça'''

tela_lar = 720  # [0]
tela_alt = 480  # [1]
pixel_tamanho = 10


def colisao(pos1, pos2):
    return pos1 == pos2


def limites(pos):
    if 0 <= pos[0] < tela_lar and 0 <= pos[1] < tela_alt:
        return False
    else:
        return True


def randomiza():
    x = random.randint(0, tela_lar)
    y = random.randint(0, tela_alt)
    return x // pixel_tamanho * pixel_tamanho, y // pixel_tamanho * pixel_tamanho


pygame.init()  # Inicia o pygame

tela = pygame.display.set_mode((tela_lar, tela_alt))  # Criar a janela
pygame.display.set_caption('Jogo da Snake!')


# a cobrinha pode ser representado por uma lista, cada elemento sendo uma posição.
cobra_xy = [(250, 50), (260, 50), (270, 50)]
cobra = pygame.Surface((pixel_tamanho, pixel_tamanho))  # criando a cobra
cobra.fill((255, 255, 255))  # dando cor a cobra
cobra_direcao = pygame.K_LEFT  # A variável vai receber uma tecla por padrão.

maca = pygame.Surface((pixel_tamanho, pixel_tamanho))
maca.fill((255, 0, 0))
maca_xy = randomiza()


def reiniciar():
    global cobra_xy
    global maca_xy
    global cobra_direcao
    cobra_xy = [(250, 50), (260, 50), (270, 50)]
    cobra_direcao = pygame.K_LEFT
    maca_xy = randomiza()


# Laço principal do jogo
while True:
    pygame.time.Clock().tick(10)  # Diminui o FPS do jogo, uma coisa útil!

    tela.fill((0, 0, 0))
    for evento in pygame.event.get():  # área de eventos do jogo
        if evento.type == pygame.QUIT:  # permite fechar a janela pelo X
            sys.exit()

        elif evento.type == pygame.KEYDOWN:
            if evento.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                # Vai verificar se o tipo de evento é algum dos que está dentro da lista;
                cobra_direcao = evento.key

    tela.blit(maca, maca_xy)

    if colisao(maca_xy, cobra_xy[0]):
        cobra_xy.append((-10, -10))
        maca = randomiza()

    for posicao in cobra_xy:
        tela.blit(cobra, posicao)

    for i in range(len(cobra_xy) - 1, 0, -1):
        if colisao(cobra_xy[0], cobra_xy[i]):
            reiniciar()

        cobra_xy[i] = cobra_xy[i-1]

    if limites(cobra_xy[0]):
        reiniciar()

    if cobra_direcao == pygame.K_UP:
        cobra_xy[0] = (cobra_xy[0][0], cobra_xy[0][1] - pixel_tamanho)

    elif cobra_direcao == pygame.K_DOWN:
        cobra_xy[0] = (cobra_xy[0][0], cobra_xy[0][1] + pixel_tamanho)

    elif cobra_direcao == pygame.K_LEFT:
        cobra_xy[0] = (cobra_xy[0][0] - pixel_tamanho, cobra_xy[0][1])

    elif cobra_direcao == pygame.K_RIGHT:
        cobra_xy[0] = (cobra_xy[0][0] + pixel_tamanho, cobra_xy[0][1])

    pygame.display.update()
