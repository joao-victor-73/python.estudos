"""
Com base no exercicio 071 do mundo 2 de Pyhton 3, vou tentar fazer um projeto de caixa eletronico
em que ele vai sacar dinheiro, depositar dinheiro e visualizar o extrato bancário.
"""

from bibliotecas.interface import *
from bibliotecas.validacao import *
from time import sleep

# v0.2 --> 02/02/2023
cabecalho('SISTEMA DE CAIXA ELETRONICO V0.2')

# print('>>> Você deseja acessar a conta bancária por qual método?')
while True:
    resposta1 = menu1(['ACESSAR CONTA PELO CPF', 'ACESSAR CONTA PELO ID', 'OUTRAS OPÇÕES', 'CANCELAR'])

    if resposta1 == 1:
        cabecalho('OPÇÃO PELO CPF')

    if resposta1 == 2:
        n = leiaID('Digite seu ID: ')

    if resposta1 == 3:
        while True:
            outra_resposta = menu3(['ABRIR CONTA', 'FAZER DEPOSITO', 'MENU ANTERIOR'])

            if outra_resposta == 1:
                cabecalho('ABRIR CONTA')

            if outra_resposta == 2:
                cabecalho('FAZER DEPOSITO')
            
            if outra_resposta == 3:
                cabecalho('VOLTANDO AO MENUR ANTERIOR')
                break

    if resposta1 == 4:
        cabecalho('OPERAÇÃO CANCELADA PELO USUÁRIO!')
        break