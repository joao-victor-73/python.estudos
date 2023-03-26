import pygame
import sys
from random import randint
from configs import Configurações, Musicas, Cores
import mensagem as mensagem
import funcoes_jogo as fj

# tentar fazer modularização com esse código depois !!!!
""" FALTA ORGANIZAR MELHOR ESSE CÓDIGO!!!!!!"""

''' CRIAR FUNÇÃO PARA A MENSAGEM DE MORTE'''

config = Configurações()
musicas = Musicas()
cor = Cores()


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


pygame.init()  # -> Inicializar o pygame

# config.musica_background


# Criando váriaveis para X e Y
x_cobra = ((config.tela_largura/2) - (80 / 2))
y_cobra = ((config.tela_altura/2) - (60 / 2))
# em x foi feito um calcúlo para deixar o objeto no meio da tela
# largura_tela / 2 - 80 / 2 -> 80 é a largura do objeto que vai ficar no meio!

x_controle = config.velocidade
y_controle = 0

# X e Y do retângulo 2
x2 = randint(40, 600)
y2 = randint(50, 430)


tela = pygame.display.set_mode((config.tela_largura, config.tela_altura))
# 640 largura / 480 altura (pode-se criar variáveis separadas para a lar e alt)

# Alterar nome da janela que for criada:
pygame.display.set_caption('JOGINHO DA PLAYLIST!')

lista_cobra = []  # lista que vai servir para guardar os aumentos da cobra!

game_over = False


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY vai ser igual a uma lista [].
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(tela, cor.verde, (XeY[0], XeY[1], 20, 20))


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
    cobra = pygame.draw.rect(tela, cor.verde, (x_cobra, y_cobra, 20, 20))
    ret2 = pygame.draw.rect(tela, cor.azul, (x2, y2, 10, 10))

    # trabalhando as colisões
    if cobra.colliderect(ret2):
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
    if lista_cobra.count(lista_cabeca) > 1:
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

    # Modificar depois para o jogo encerrar quando tocar na lateral
    # No momento, quando a cobra passar da tela, ela irá pro outro lado;
    if x_cobra > config.tela_largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = config.tela_largura

    if y_cobra < 0:
        y_cobra = config.tela_altura
    if y_cobra > config.tela_altura:
        y_cobra = 0

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
    tela.blit(mensagem.mensagem_pontos(), (470, 10))

    # Esse comando abaixo vai servir p/ que a cada interação com o looping principal
    # do jogo, ele atualiza a tela do jogo.
    pygame.display.update()
