'''< A função reduce() em Python é uma função da biblioteca functools que aplica
uma determinada função binária a pares consecutivos de elementos em uma estrutura
de dados iterável (como uma lista, tupla ou outro objeto iterável), 
reduzindo-a a um único valor. >'''

# Importando a biblioteca functools
from functools import reduce


def soma(a, b):
    # Criando uma função para somar
    x = a + b
    return x


# Criando uma lista:
lista = [47, 11, 42, 13]

# Usando reduce com uma função e uma lista. A função vai retornar o valor máximo
print(reduce(soma, lista))

# Usando a função reduce() com lambda
print(f'Resultado com lambda: {reduce(lambda x, y: x+y, lista)}')
