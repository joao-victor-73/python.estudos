import pygame
import sys
from random import randint
from configs import Configurações, Musicas, Cores
from mensagem import Mensagens
from cobra import Cobra
import funcoes as f

# tentar fazer modularização com esse código depois !!!!
""" FALTA ORGANIZAR MELHOR ESSE CÓDIGO!!!!!!"""


config = Configurações()
musicas = Musicas()
cor = Cores()


def reiniciar():
    global pontos, velocidade, cont, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x2, y2, morreu

    pontos = cont = 0
    velocidade = 10
    comprimento_inicial = 5

    x_cobra = ((config.tela_largura/2) - (80 / 2))
    y_cobra = ((config.tela_altura/2) - (60 / 2))

    lista_cabeca = []
    lista_cobra = []

    x2 = randint(40, 600)
    y2 = randint(50, 430)

    morreu = False


pygame.init()  # -> Inicializar o pygame


x_controle = config.velocidade
y_controle = 0

# X e Y do retângulo 2
x2 = randint(40, 600)
y2 = randint(50, 430)


fonte = pygame.font.SysFont('Arial', 25, True, True)  # variável para fonte
# parâmetros -> 1ª: Tipo da fonte / 2ª Tamanho / 3ª Se vai estar em negrito / 4ª Em italico


tela = pygame.display.set_mode((config.tela_largura, config.tela_altura))
# 640 largura / 480 altura (pode-se criar variáveis separadas para a lar e alt)

# Alterar nome da janela que for criada:
pygame.display.set_caption('JOGINHO DA PLAYLIST!')

lista_cobra = []  # lista que vai servir para guardar os aumentos da cobra!


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY vai ser igual a uma lista [].
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(tela, cor.verde, (XeY[0], XeY[1], 20, 20))


    # Laço princípal do jogo
while True:

    cobra = Cobra(config, tela, cor)

    pygame.time.Clock().tick(10)  # Diminui o FPS do jogo, uma coisa útil!
    tela.fill(config.tela_cor)

    men_game_over = 'Game Over! Pressione "R" para jogar novamente!'

    msg = Mensagens(config, men_game_over, tela, cor)

    mensagem = f'Pontos: {config.pontos}'
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))

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

    cobra.x_cobra += x_controle
    cobra.y_cobra += y_controle

    '''
    # Comandos para fazer o objeto se mover por conta do usuário!
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        x_cobra -= velocidade

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x_cobra += velocidade

    if pygame.key.get_pressed()[pygame.K_UP]:
        y_cobra -= velocidade

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        y_cobra += velocidade
    '''

    # Retângulos:
    cobra = cobra.desenhar_cobra()
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
        velocidade = 20

    # Funcionalidade para fazer a cobra crescer a medida que come os pontos!
    lista_cabeca = []
    lista_cabeca.append(cobra.x_cobra)
    lista_cabeca.append(cobra.y_cobra)

    lista_cobra.append(lista_cabeca)

    # Essa condição vai dizer que a cabeça da cobra escostou nela mesma! Ou que ela saiu da tela
    if lista_cobra.count(lista_cabeca) > 1 or ((cobra.x_cobra > config.tela_largura or cobra.x_cobra < 0) or (cobra.y_cobra < 0 or cobra.y_cobra > config.tela_altura)):

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

            msg.monstrar_mensagem()
            pygame.display.update()

    if len(lista_cobra) > config.comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    """    
    # Fazendo com que o objeto fique voltando pro inicio
    if y >= altura_tela:
        y = 0

    y += 0.1  # Vai fazer o objeto andar na linha y
    """

    # Vai fazer mostrar na tela o texto!
    tela.blit(texto_formatado, (470, 10))

    # Esse comando abaixo vai servir p/ que a cada interação com o looping principal
    # do jogo, ele atualiza a tela do jogo.
    pygame.display.update()
