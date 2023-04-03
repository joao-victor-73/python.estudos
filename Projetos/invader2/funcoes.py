import sys
import pygame
from projetil import Projetil
from alien import Alien


def press_tecla(evento, configs, tela, nave, projeteis):
    # Responde a pressionamento de tecla
    if evento.key == pygame.K_RIGHT:
        # Move a espaçonave para a direita
        nave.mover_direita = True  # vai fazer efeito na def atualizar na classe nave

    elif evento.key == pygame.K_LEFT:
        nave.mover_esquerda = True

    elif evento.key == pygame.K_q:  # Precione 'Q' para sair
        sys.exit()

    elif evento.key == pygame.K_c:  # Atirar!
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


def atualizacao_tela(configs, tela, nave, aliens, projeteis):
    # Os nomes dos parâmetros são os mesmos para falicitar!
    tela.fill(configs.fundo_tela)

    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas.
    for projetil in projeteis.sprites():
        projetil.desenha_projetil()

    nave.blitme()  # Faz a nave aparecer na tela
    aliens.draw(tela)  # Faz o alien aparecer na tela

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


def aliens_em_y(configs, nave_altura, alien_altura):
    ''' Determina o número de linhas com alienígenas que cabem na tela.'''

    space_avaliado_y = (configs.tela_altura - (3 * alien_altura) - nave_altura)
    num_linhas_y = int(space_avaliado_y / (2 * alien_altura))

    return num_linhas_y


def aliens_em_x(configs, alien_largura):
    # Determina o número de alienígenas que cabem em uma linha.
    space_avaliado_x = configs.tela_largura - 2 * alien_largura
    num_aliens_x = int(space_avaliado_x / (2 * alien_largura))

    return num_aliens_x


def criar_alien(configs, tela, aliens, alien_num, num_linhas_y):
    # Cria alienígena e o posiciona na linha
    alien = Alien(configs, tela)

    alien_largura = alien.rect.width

    alien.x = alien_largura + 2 * alien_largura * alien_num
    alien.rect.x = alien.x

    alien.rect.y = alien.rect.height + 2 * alien.rect.height * num_linhas_y

    aliens.add(alien)


def criar_frota(configs, tela, nave, aliens):  # Cria uma frota de alienigenas;
    '''Cria um alienígena e calcula o número de alienígenas em uma linha.'''
    alien = Alien(configs, tela)

    aliens_x = aliens_em_x(configs, alien.rect.width)
    aliens_y = aliens_em_y(
        configs, nave.retangulo.height, alien.rect.height)

    # Cria a primeira linha de alienígenas
    for alien_linha in range(aliens_y):
        for alien_reto in range(aliens_x):
            # Cria um alienígena e o posiciona na linha
            criar_alien(configs, tela, aliens, alien_reto, alien_linha)



def check_frota_borda(configs, aliens):
    ''' Responde apropriadamente se algum alienígena alcançou uma borda. '''
    for alien in aliens.sprites():
        if alien.checando_borda():
            mudar_direcao_frota(configs, aliens)
            break


def mudar_direcao_frota(configs, aliens):
    ''' Faz toda a frota descer e muda a sua direção. '''
    for alien in aliens.sprites():
        alien.rect.y += configs.frota_velocidade
    configs.frota_direcao *= -1



def atualizar_aliens(configs, aliens):
    '''
    Verifica se a frota está em uma das bordas e então
    atualiza as posições de todos os alienígenas da frota.
    '''
    check_frota_borda(configs, aliens)
    aliens.update()
