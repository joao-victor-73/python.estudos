""" 03/05/2025
Desafio 1: Contador de vogais

Crie uma função chamada contar_vogais que recebe uma string como parâmetro e 
retorna quantas vogais (a, e, i, o, u) existem nessa string.
"""

texto = str(input('Digite uma frase: '))

def contar_vogais(msg):
    cont = 0
    for p in msg.lower():
        if p in 'aeiou':
            cont += 1
    return cont

print(contar_vogais(texto))