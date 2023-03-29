import sys
import pygame
from projetil import Projetil


def press_tecla(evento, configs, tela, nave, projeteis):
    # Responde a pressionamento de tecla
    if evento.key == pygame.K_RIGHT:
        # Move a espaçonave para a direita
        nave.mover_direita = True  # vai fazer efeito na def atualizar na classe nave

    elif evento.key == pygame.K_LEFT:
        nave.mover_esquerda = True

    elif evento.key == pygame.K_w:  # Atirar!
        def atirar_projetil(configs, tela, nave, projeteis):
            # Dispara um projétil se o limite ainda não foi alcançado.

            # Cria um novo projétil e o adiciona ao grupo de projéteis.
            if len(projeteis) < configs.projeteis_permitidos:
                novo_projetil = Projetil(configs, tela, nave)
                projeteis.add(novo_projetil)

        atirar_projetil(configs, tela, nave, projeteis)


def soltar_teca(evento, nave):
    # Responde quando soltar uma tecla
    if evento.key == pygame.K_RIGHT:
        nave.mover_direita = False

    elif evento.key == pygame.K_LEFT:
        nave.mover_esquerda = False


def checar_eventos(configs, tela, nave, projeteis):
    # Responde a eventos de pressionamento de teclas e de mouse
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

        elif evento.type == pygame.KEYDOWN:
            press_tecla(evento, configs, tela, nave, projeteis)

        elif evento.type == pygame.KEYUP:
            soltar_teca(evento, nave)


def atualizacao_tela(configs, tela, nave, projeteis):
    # Os nomes dos parâmetros são os mesmos para falicitar!
    tela.fill(configs.fundo_tela)

    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas.
    for projetil in projeteis.sprites():
        projetil.desenha_projetil()

    nave.blitme()  # Faz a nave aparecer na tela

    pygame.display.flip()  # Deixa a tela recente vísivel.


# Atualiza a posição dos projéteis e se livra dos projéteis antigos.
def atualizar_projeteis(projeteis):

    # Atualiza as posições dos projéteis;
    projeteis.update()

    # Livra-se dos projéteis que desapareceram
    for projetil in projeteis.copy():
        if projetil.ret_p.bottom <= 0:
            projeteis.remove(projetil)
            print(len(projeteis))
