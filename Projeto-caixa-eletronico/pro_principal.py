"""
Com base no exercicio 071 do mundo 2 de Pyhton 3, vou tentar fazer um projeto de caixa eletronico
em que ele vai sacar dinheiro, depositar dinheiro e visualizar o extrato bancário.
"""

from bibliotecas.interface import *

cabecalho('SISTEMA DE CAIXA ELETRONICO V0.2')

# print('>>> Você deseja acessar a conta bancária por qual método?')
while True:
    resposta1 = menu1(['ACESSAR PELO CPF', 'ACESSAR PELO ID', 'OUTRAS OPÇÕES', 'CANCELAR'])

    if resposta1 == 1:
        cabecalho('OPÇÃO PELO CPF')
    if resposta1 == 2:
        cabecalho('OPÇÃO PELO ID')
    if resposta1 == 3:
        cabecalho('OUTRAS OPÇÕES')
    if resposta1 == 4:
        cabecalho('OPERAÇÃO CANCELADA PELO USUÁRIO!')
        break