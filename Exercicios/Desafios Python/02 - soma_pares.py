""" 06/05/2025
Desafio 2: Soma dos números pares

Crie uma função chamada soma_pares que receba uma lista 
de números inteiros e retorne a soma de todos os números pares da lista.

Regras:
    -> Pode usar for ou compreensão de listas (list comprehension).

    -> Não precisa validar o tipo dos dados (assuma que a lista só tem inteiros).
"""

lista_numeros = [2, 15, 25, 84, 12, 1234, 952, 9]


def soma_pares(lista):
    soma = 0
    apenas_par = []

    for num in lista:
        if num % 2 == 0:
            apenas_par.append(num)
            soma += num

    print(f"A lista digitada é: {lista_numeros}")
    print(f"Dentro dessa lista, os números pares são: {apenas_par}")
    print(f"E essa é a soma de todos os números pares: {soma}")
    return soma


soma_pares(lista_numeros)
