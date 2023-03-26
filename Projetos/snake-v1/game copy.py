import pygame
import sys
from random import randint
from configs import Configurações, Musicas

# tentar fazer modularização com esse código depois !!!!
""" FALTA ORGANIZAR MELHOR ESSE CÓDIGO!!!!!!"""

''' CRIAR FUNÇÃO PARA A MENSAGEM DE MORTE'''

config = Configurações()
musicas = Musicas()


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

# config.musica_background


# Isso aqui depois pode ser colocado em uma função ou em um dicionário
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Criando váriaveis para X e Y
x_cobra = ((config.tela_largura/2) - (80 / 2))
y_cobra = ((config.tela_altura/2) - (60 / 2))
# em x foi feito um calcúlo para deixar o objeto no meio da tela
# largura_tela / 2 - 80 / 2 -> 80 é a largura do objeto que vai ficar no meio!

velocidade = 10  # variável para velocidade do objeto
x_controle = velocidade
y_controle = 0

# X e Y do retângulo 2
x2 = randint(40, 600)
y2 = randint(50, 430)

pontos = 0  # variável para armazenar a pontuação
cont = 0  # Variável para tocar música de 10 pontos

fonte = pygame.font.SysFont('Arial', 25, True, True)  # variável para fonte
# parâmetros -> 1ª: Tipo da fonte / 2ª Tamanho / 3ª Se vai estar em negrito / 4ª Em italico


tela = pygame.display.set_mode((config.tela_largura, config.tela_altura))
# 640 largura / 480 altura (pode-se criar variáveis separadas para a lar e alt)

# Alterar nome da janela que for criada:
pygame.display.set_caption('JOGINHO DA PLAYLIST!')

lista_cobra = []  # lista que vai servir para guardar os aumentos da cobra!
comprimento_inicial = 5

game_over = False


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY vai ser igual a uma lista [].
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(tela, verde, (XeY[0], XeY[1], 20, 20))


    # Laço princípal do jogo
while True:
    pygame.time.Clock().tick(10)  # Diminui o FPS do jogo, uma coisa útil!
    tela.fill(config.tela_cor)

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))

    # o lopping for vai servir para checar os eventos!
    for evento in pygame.event.get():
        # Vai servir para poder fechar a janela
        if evento.type == pygame.QUIT:
            sys.exit()

        # Vai fazer com que a cobra fique em constante movimento.
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if evento.key == pygame.K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if evento.key == pygame.K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if evento.key == pygame.K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle

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
    cobra = pygame.draw.rect(tela, verde, (x_cobra, y_cobra, 20, 20))
    ret2 = pygame.draw.rect(tela, azul, (x2, y2, 10, 10))

    # trabalhando as colisões
    if cobra.colliderect(ret2):
        x2 = randint(40, 600)
        y2 = randint(50, 430)
        # cada vez que o retangulo 1 colider com o outro, os valores X e Y serão
        # randimicamentes alterados

        pontos += 1  # toda vez que houver colisão, os pontos vão subir

        comprimento_inicial += 1

        # Coisa extra: toda vez que coletar 10 pontos, ele toca uma outra música
        cont += 1
        if cont == 10:
            musicas.musica_10pontos.play()
            cont = 0
        else:
            # O barulho de colisão apenas rodará quando ouver colisão
            musicas.musica_coleta.play()

    # Vai deixar o jogo mais rapido quando atingir determinado x pontos
    if pontos >= 20:
        velocidade = 20

    # Funcionalidade para fazer a cobra crescer a medida que come os pontos!
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    # Essa condição vai dizer que a cabeça da cobra escostou nela mesma!
    if lista_cobra.count(lista_cabeca) > 1:
        fonte_over = pygame.font.SysFont('arial', 15, True, True)
        mensagem_over = 'Game Over! Precione "R" para jogar novamente!'
        texto_over_formatado = fonte_over.render(
            mensagem_over, True, (0, 0, 0))
        ret_texto = texto_over_formatado.get_rect()

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

            ret_texto.center = (config.tela_largura // 2,
                                config.tela_altura // 2)
            tela.blit(texto_over_formatado, ret_texto)
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

    if len(lista_cobra) > comprimento_inicial:
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
