# Trabalhando com o módulo random (aulas 295, 296)

import random

# random.randrange(inicio, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico;
n1 = random.randrange(1, 10, 2)
print(f'Nº Aleatórios COM passo: {n1}')

# random.randint(inicio, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo";
n2 = random.randint(1, 10)
print(f'Nº Aleatórios SEM passo: {n2}')

# random.uniform(inicio, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo";
n3 = random.uniform(1, 10)
print(f'Nº Aleatórios FLUTUANTES: {n3}')

# random.shuffle(SequenciaMutável)
#   -> Embaralha a lista original (não retorna a sequencia original);
nomes = ['Luiz', 'Otaviana', 'Amara', 'Grivalda']
random.shuffle(nomes)
print(f'Lista de nomes embaralhados: {nomes}')

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete);
#       -> Usaremos como exemplo a lista anterior para ele pegar valores
#          aleatórios e colocar em uma nova lista.
novos_nomes = random.sample(nomes, k=2)
print('=' * 30)
print(f'Lista de Nomes: {nomes}')
print(f'Lista de Novos Nomes: {novos_nomes}')

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores);
#       -> Mesma coisa do sample, mas a diferença é que pode vir valores
#          da lista repetidos.


# random.choice(Iterável)
#   -> Escolhe um elemento do iterável;
print(f'Escolha apenas um valor da lista: {random.choice(nomes)}')
