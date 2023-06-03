'''
Vai ser criado um menu para a escolha:
    - Da dificuldade;
    - Do tipo das palavras;
    - Um jogador, ou dois jogadores;
'''


def escolha_categoria():
    from time import sleep

    print('+', '-' * 60, '+')
    print(f"{'Bem-vindo(a) ao >>JOGO DA FORCA<<':^65}")
    print('+', '-' * 60, '+')

    print(f"""\n{'| >>> CATEGORIA DAS PALAVRAS <<<|':^65}
\n\t[ 1 ] - FRUTAS
\t[ 2 ] - COMIDAS
\t[ 3 ] - CIDADES
\t[ 4 ] - ANIMAIS
\t[ 5 ] - ALEATÓRIOS
          """)

    try:
        opcao_categoria = int(input("Digite a opção: "))
        if (opcao_categoria == 1) or (opcao_categoria == 2) or (opcao_categoria == 3) or (opcao_categoria == 4) or (opcao_categoria == 5):
            return opcao_categoria

        else:
            print(
                f"{'|>>> Você digitou um valor diferente das opções disponíveis <<<|':^65}")
            sleep(2)

            escolha_categoria()

    except ValueError:
        # mensagem temporária
        print("ERRO DE VALOR ENCONTRADO! \nTente novamente!")
        sleep(2)

        escolha_categoria()
