from time import sleep


def leiaInt(valor):
    while True:
        try:
            n = int(input(valor))
        except (ValueError, TypeError):
            print('ERRO ENCONTRADO! - Por favor digite uma opção válida!')
        except KeyboardInterrupt:
            print('O USUÁRIO decidiu não digitar nenhum valor!')
            return 0
        else:
            return n 


def traco(tam=40):
    # função que vai criar um traço para cabeçalho ou separar algo.
    # o seu parâmetro padrão será de tamanho 40.
    return '-' * 40


def cabecalho(msg):
    print(traco())
    print(msg.center(40))
    print(traco())
    # Vai entrar o traço, logo depois a a mensagem desejada centralizada com a quant de traços.


def menu1(lista):
    # O menu1 vai servir para adentrar no sistema de caixa eletrônico
    cabecalho('ACESSANDO SUA CONTA BANCÁRIA')
    c = 1  # essa variável vai servir como um índice de opção
    for item in lista:
        print(f'{c} -- {item}')
        c += 1
        sleep(0.5)
    print(traco())
    opcao = leiaInt('Qual a sua opção? ')
    return opcao


def menu3(lista):
    # O menu3 vai servir para acessar as outras opções
    cabecalho('OUTRAS OPÇÕES')
    c = 1
    for item in lista:
        print(f'{c} -- {item}')
        c += 1
        sleep(0.5)
    print(traco())
    opcao = leiaInt('Qual sua opção? ')
    return opcao


def tela_espera(msg):
    cabecalho(msg)
    sleep(2)