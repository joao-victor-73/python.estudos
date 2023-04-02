import pygame
import sys
from random import randint
from configs import Configurações, Musicas, Cores
from cobra import Cobra
import mensagem as mensagem
import funcoes as f

# tentar fazer modularização com esse código depois !!!!
""" FALTA ORGANIZAR MELHOR ESSE CÓDIGO!!!!!!"""

''' CRIAR FUNÇÃO PARA A MENSAGEM DE MORTE'''

config = Configurações()
musicas = Musicas()
cor = Cores()


pygame.init()  # -> Inicializar o pygame


# Criando váriaveis para X e Y
x_cobra = ((config.tela_largura/2) - (80 / 2))
y_cobra = ((config.tela_altura/2) - (60 / 2))

x_controle = config.velocidade
y_controle = 0

# X e Y da maçã
x2 = randint(40, 600)
y2 = randint(50, 430)


tela = pygame.display.set_mode((config.tela_largura, config.tela_altura))
# 640 largura / 480 altura (pode-se criar variáveis separadas para a lar e alt)

# Altera nome da janela:
pygame.display.set_caption('JOGINHO DA PLAYLIST!')

lista_cobra = []  # lista que vai servir para guardar os aumentos da cobra!


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY vai ser igual a uma lista [].
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(tela, cor.verde, (XeY[0], XeY[1], 20, 20))


cobra = Cobra(config, tela, cor)

# Laço princípal do jogo
while True:
    pygame.time.Clock().tick(10)  # Diminui o FPS do jogo, uma coisa útil!
    tela.fill(config.tela_cor)

    # o lopping for vai servir para checar os eventos!
    for evento in pygame.event.get():
        # Vai servir para poder fechar a janela
        if evento.type == pygame.QUIT:
            sys.exit()

        # Vai fazer com que a cobra fique em constante movimento.
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                if x_controle == config.velocidade:
                    pass
                else:
                    x_controle = -config.velocidade
                    y_controle = 0

            if evento.key == pygame.K_RIGHT:
                if x_controle == -config.velocidade:
                    pass
                else:
                    x_controle = config.velocidade
                    y_controle = 0

            if evento.key == pygame.K_UP:
                if y_controle == config.velocidade:
                    pass
                else:
                    y_controle = -config.velocidade
                    x_controle = 0

            if evento.key == pygame.K_DOWN:
                if y_controle == -config.velocidade:
                    pass
                else:
                    y_controle = config.velocidade
                    x_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle

    # Retângulos:
    # cobra = pygame.draw.rect(tela, cor.verde, (cobra.x, cobra.y, 20, 20))
    ret2 = pygame.draw.rect(tela, cor.azul, (x2, y2, 10, 10))

    # trabalhando as colisões
    if cobra.cobra.colliderect(ret2):
        x2 = randint(40, 600)
        y2 = randint(50, 430)
        # cada vez que o retangulo 1 colider com o outro, os valores X e Y serão
        # randimicamentes alterados

        config.pontos += 1  # toda vez que houver colisão, os pontos vão subir

        config.comprimento_inicial += 1

        # Coisa extra: toda vez que coletar 10 pontos, ele toca uma outra música
        config.cont += 1
        if config.cont == 10:
            musicas.musica_10pontos.play()
            config.cont = 0
        else:
            # O barulho de colisão apenas rodará quando ouver colisão
            musicas.musica_coleta.play()

    # Vai deixar o jogo mais rapido quando atingir determinado x pontos
    if config.pontos >= 20:
        config.velocidade = 20

    # Funcionalidade para fazer a cobra crescer a medida que come os pontos!
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    # Essa condição vai dizer que a cabeça da cobra escostou nela mesma!
    f.encostou_na_cabeca(lista_cobra, lista_cabeca, config, cor, tela)

    # Se enconstar nas laterais, a cobra morre!
    f.encostou_borda(x_cobra, y_cobra, config, cor, tela)

    if len(lista_cobra) > config.comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    """    
    # Fazendo com que o objeto fique voltando pro inicio
    if y >= altura_tela:
        y = 0

    y += 0.1  # Vai fazer o objeto andar na linha y
    """

    # Vai fazer mostrar na tela o texto de pontos!
    tela.blit(mensagem.mensagem_pontos(config.pontos), (470, 10))

    # Esse comando abaixo vai servir p/ que a cada interação com o looping principal
    # do jogo, ele atualiza a tela do jogo.
    pygame.display.update()
