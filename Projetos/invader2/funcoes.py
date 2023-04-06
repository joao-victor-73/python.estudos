import sys
import pygame
from time import sleep
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


def atualizar_projeteis(configs, tela, nave, aliens, projeteis):
    # Atualiza a posição dos projéteis e se livra dos projéteis antigos.

    # Atualiza as posições dos projéteis;
    projeteis.update()

    # Livra-se dos projéteis que desapareceram
    for projetil in projeteis.copy():
        if projetil.rect.bottom <= 0:
            projeteis.remove(projetil)
            print(len(projeteis))

    # check_bullet_alien_collisions
    checa_se_acertou_alien(configs, tela, nave, aliens, projeteis)


def checa_se_acertou_alien(configs, tela, nave, aliens, projeteis):
    # Verifica se algum projétil atingiu os alienígenas
    # Em caso afirmativo, livra-se do projétil e do alienígena.
    collisions = pygame.sprite.groupcollide(projeteis, aliens, True, True)

    if len(aliens) == 0:
        # Destrói os projéteis existentes e cria uma nova frota
        projeteis.empty()
        criar_frota(configs, tela, nave, aliens)


def aliens_em_y(configs, nave_altura, alien_altura):
    ''' Determina o número de linhas com alienígenas que cabem na tela.'''

    space_avaliado_y = (configs.tela_altura -
                        (2.50 * alien_altura) - nave_altura)
    num_linhas_y = int(space_avaliado_y / (1.25 * alien_altura))

    return num_linhas_y


def aliens_em_x(configs, alien_largura):
    # Determina o número de alienígenas que cabem em uma linha.
    space_avaliado_x = configs.tela_largura - 1.25 * alien_largura
    num_aliens_x = int(space_avaliado_x / (1.25 * alien_largura))

    return num_aliens_x


def criar_alien(configs, tela, aliens, alien_num, num_linhas_y):
    # Cria alienígena e o posiciona na linha
    alien = Alien(configs, tela)

    alien_largura = alien.rect.width

    # Determina a distância dos aliens um do outro (alterar apenas os números)
    alien.x = alien_largura + 1.25 * alien_largura * alien_num
    alien.rect.x = alien.x

    alien.rect.y = alien.rect.height + 1.25 * alien.rect.height * num_linhas_y

    aliens.add(alien)


def criar_frota(configs, tela, nave, aliens):  # Cria uma frota de alienigenas;
    '''Cria um alienígena e calcula o número de alienígenas em uma linha.'''
    alien = Alien(configs, tela)

    aliens_x = aliens_em_x(configs, alien.rect.width)
    aliens_y = aliens_em_y(
        configs, nave.rect.height, alien.rect.height)

    # Cria a primeira linha de alienígenas
    for alien_linha in range(aliens_y):
        for alien_reto in range(aliens_x):
            # Cria um alienígena e o posiciona na linha
            criar_alien(configs, tela, aliens, alien_reto, alien_linha)


def check_frota_borda(configs, aliens):  # check_fleet_edges
    ''' Responde apropriadamente se algum alienígena alcançou uma borda. '''
    for alien in aliens.sprites():
        if alien.checando_borda():
            mudar_direcao_frota(configs, aliens)
            break


def mudar_direcao_frota(configs, aliens):  # change_fleet_direction
    ''' Faz toda a frota descer e muda a sua direção. '''
    for alien in aliens.sprites():
        alien.rect.y += configs.frota_velocidade
    configs.frota_direcao *= -1


def nave_hit(configs, stats, tela, nave, aliens, projeteis):
    ''' Responde ao fato de a espaçonave ter sido atingida por um alienígena. '''

    if stats.nave_esquerda > 0:  # verifica se o jogador ainda tem espaçonave
        # Decrementa nave_limite
        stats.nave_esquerda -= 1

        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        projeteis.empty()

        # Cria uma nova frota e centraliza a espaçonave
        criar_frota(configs, tela, nave, aliens)
        nave.centro_nave()

        # Faz uma pausa para recriar o jogo
        sleep(1)

    else:
        stats.game_active = False


def checa_alien_borda_inferior(configs, stats, tela, nave, aliens, projeteis):
    ''' Verifica se algum alien alcançou a borda inferior da tela. '''
    tela_retangulo = tela.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= tela_retangulo.bottom:
            # Trata esse caso do mesmo modo que é feito quando a espaço nave é atingida
            nave_hit(configs, stats, tela, nave, aliens, projeteis)
            break


def atualizar_aliens(configs, stats, tela, nave, aliens, projeteis):
    '''
    Verifica se a frota está em uma das bordas e então
    atualiza as posições de todos os alienígenas da frota.
    '''
    check_frota_borda(configs, aliens)
    aliens.update()

    # Verifica se houve colisões entre alienígenas e a espaçonave
    if pygame.sprite.spritecollideany(nave, aliens):
        nave_hit(configs, stats, tela, nave, aliens, projeteis)

    # Verifica se há algum alienígena que atengiu a parte inferior da tela
    checa_alien_borda_inferior(configs, stats, tela, nave, aliens, projeteis)
