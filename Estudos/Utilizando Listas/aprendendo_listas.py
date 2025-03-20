"""
A lista serve para armazenar informações complexas de forma organizada.

Uma lista é uma estrutura de dados muito flexível. 
Você pode editá-las, organizá-las, ampliá-las ou encurtá-las através de vários métodos.
"""

lista_homogenea = ["um", "dois", "três"]
lista_heterogenea = [1.43, 2, "três", ["outra", "lista"]]

print(lista_homogenea)
print(lista_heterogenea)

# Acessando elementos de uma lista
frutas = ['Uva', 'Maça', 'Banana', 'Abacaxi']

print(frutas[3])  # Abacaxi
print(frutas[0])  # Uva


# Adicionando elementos na lista

# Append
frutas.append('Laranja')
print(frutas)  # ['Uva', 'Maça', 'Banana', 'Abacaxi', 'Laranja']


# Insert - Adiciona um elemento em uma posição especifica
frutas.insert(1, 'Goiaba')  # Vou adicionar o elemento antes de 'Maça'
print(frutas)  # ['Uva', 'Goiaba', 'Maça', 'Banana', 'Abacaxi', 'Laranja']


# Juntando duas listas
compras = ['Cebola', 'Pepino', 'Alface', 'Batata']
compras.extend(frutas)

print(f'A lista de compras é: {compras}')
# A lista de compras é: ['Cebola', 'Pepino', 'Alface', 'Batata', 'Uva', 'Goiaba', 'Maça', 'Banana', 'Abacaxi', 'Laranja']



# Excluindo elementos de uma lista:
print(compras)
del(compras[0:2])
print(compras) # ['Alface', 'Batata', 'Uva', 'Goiaba', 'Maça', 'Banana', 'Abacaxi', 'Laranja']

compras.remove('Alface')
print(compras) # ['Batata', 'Uva', 'Goiaba', 'Maça', 'Banana', 'Abacaxi', 'Laranja']