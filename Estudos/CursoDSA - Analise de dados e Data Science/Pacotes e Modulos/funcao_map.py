'''< A função map() em Python é uma função que aplica uma determinada função
a cada elemento de uma estrutura de dados iterável (como uma lista, tupla ou 
outro objeto iterável). 
A função map() retorna um objeto que pode ser convertido em outra estrutura de dados
como uma lista, se necessário. >'''


def potencia(x):
    # Função Python que retorna um número ao quadrado
    return x ** 2


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num_quadrados = list(map(potencia, numeros))

print(num_quadrados)

print('-' * 20, 'Exemplo 2', '-' * 20)

# Criando duas funções

# Função 1 - Recebe uma temperatura como parâmetro e retorna a temperatura em Fahrenheit


def fahrenheit(t):
    return ((float(9)/5) * t + 32)

# Função 2 - Recebe uma temperatura como parâmetro e retorna a temperatura em Celsius


def celsius(t):
    return ((float(5)/9) * (t-32))


# Criando uma lista
temperaturas = [0, 22.5, 40, 100]

# Aplicando a função a cada elemento da lista de temperaturas.
# Em Python 3, a função map() retorna um iterator
print(map(fahrenheit, temperaturas))

# Função map() retorna a lista de temperaturas converidas em Fahrenheit
print(list(map(fahrenheit, temperaturas)))
