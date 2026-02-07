""""19/05/2025
Desafio 05:
            Crie uma função chamada analisa_lista que receba uma lista de números inteiros e retorne:
                1. Os números únicos (aqueles que aparecem só uma vez)
                2. Os números repetidos (aqueles que aparecem mais de uma vez)


            Formato de saída:
                unicos, repetidos = analisa_lista([1, 2, 2, 3, 4, 4, 5, 6])
                print("Únicos:", unicos)
                print("Repetidos:", repetidos)

            Saída esperada:
                Únicos: [1, 3, 5, 6]
                Repetidos: [2, 4]


            Regras:
                -> Não usar bibliotecas como collections.
                -> Pode usar dicionários ou listas auxiliares.
                -> Os números nas listas de saída devem estar sem repetição.


"""

lista_de_numeros = [2, 3, 5, 85, 2, 25, 3, 25, 8, 9, 12, 12]

def analisa_lista(numeros):
    unicos = []
    repetidos = []
    contagem = {}


    # Primeiro faz uma contagem de todos os numeros (quantas vezes eles aparecem)
    for n in numeros:
        if n in contagem:
            contagem[n] += 1
        else:
            contagem[n] = 1

    # Aqui ele faz uma separação entre os numeros repetidos e unicos
    # percorrendo o dicionario da contagem.
    for num, qtd in contagem.items():
        if qtd == 1:
            unicos.append(num)
        else:
            repetidos.append(num)

    return unicos, repetidos

unico, repete = analisa_lista(lista_de_numeros)
print(f"Lista de Números: {lista_de_numeros}")
print(f"Numeros Unicos: {unico}")
print(f"Numeros repetidos: {repete}")