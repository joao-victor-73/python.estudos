'''< A função filter() em Python é uma função que filtra elementos de uma estrutura
de dados iterável (como uma lista, tupla ou outro objeto iterável) com base em
uma determinada condição.
A função retorna um objeto filtro, que pode ser convertido em outra estrutura de
dados, como uma lista, se necessário. >'''

# Criando uma função:
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
# Testando a função
print(verificaPar(35))
print(verificaPar(100))

# Criando uma lista
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(f'A lista completa é: {numbers}')

# A função filter retorna um iterator
print(f'Iterator: {filter(verificaPar, numbers)}')

# A função filter retornando uma lista:
print(list(filter(verificaPar, numbers)))
