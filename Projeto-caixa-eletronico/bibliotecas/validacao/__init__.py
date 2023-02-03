# Criar uma função para válidar o CPF digitado


# ---------------------------------------->>> PARTE DO ID <<<------------------------------------------------------


def leiaID(validar_id):
    # o id tem que ter 8 digitos. não menos, nem mais. E esse id vai ser entregue ao cliente que abriu a conta.
    # Na primeira versão deste projeto, o id não vai importar. Mas nas próximas versão o id vai ser gerado corretamente e entregue ao criar a conta.

    # O ID só vai permitir até 5 números!
    tentativa = 0
    while True:
        try:
            if len(validar_id) < 5 or len(validar_id) > 5:
                print('O ID DIGITOS A MAIS OU A MENOS. TENTE NOVAMENTE')
            else:
                id_valido = int(input(validar_id))

        except (ValueError, TypeError):
            print('ALGO DEU ERRADO! -- Tente novamente!')    
        except KeyboardInterrupt:
            print(f'USUÁRIO DECIDIU NÃO DIGITAR!')
            return 0
        else:
             while True:
                if id_valido <= 99999:  # vai verificar se o número digitado tem menos de 5 digitos
                    return id_valido
                else:
                    print('O ID NÃO TEM 5 DIGITOS!')
            # return id_valido

def digiteID(dig_id=0):
    from bibliotecas.interface import cabecalho
    cabecalho('ACESSANDO CONTA PELO ID')