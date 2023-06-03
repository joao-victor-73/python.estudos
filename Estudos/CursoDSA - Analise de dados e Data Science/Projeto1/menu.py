'''
Vai ser criado um menu para a escolha:
    - Da dificuldade;
                                        - Do tipo das palavras;
    - Um jogador, ou dois jogadores;
'''


def escolha_categoria():
    from time import sleep

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


def escolha_jogadores():

    print('+', '-' * 60, '+')
    print(f"{'ESCOLHA QUANTOS JOGADORES SERÃO:':^65}")
    print('+', '-' * 60, '+')

    print("""
    [ 1 ] - Um Jogador
    [ 2 ] - Dois Jogadores
    """)

    try:
        opcao_jogadores = int(input('Digite sua escolha: '))
        if (opcao_jogadores == 1) or (opcao_jogadores == 2):
            print("OPÇÃO GUARDADA...")

            if opcao_jogadores == 1:
                nome_1 = input(">>> Qual nome de jogador deseja? ")

                return opcao_jogadores, nome_1

            elif opcao_jogadores == 2:
                nome_1 = input(">>> Qual nome do 1º jogador? ")
                nome_2 = input(">>> Qual nome do 2º jogador? ")

                return opcao_jogadores, nome_1, nome_2

    except ValueError:
        print("O QUE FOI DIGITADO DEU UM ERRO DE VALOR. \nPOR FAVOR, TENTE NOVAMENTE")
        escolha_jogadores()
