"""
Um dicionário em Python é uma coleção de pares chave-valor – denotada na literatura 
pelos termos em inglês key:value. 

Cada chave é conectada a um valor, e você pode usar uma chave para acessar o valor associado a ela. 
"""

compras = {"Maca": 2, "Banana": 3, "Uva": 10}
print(compras)


# Adicionando elementos em um dicionário
compras['Laranja'] = 4
print(compras)

# A mesma coisa vale para alterar um valor do dicionário
compras['Maca'] = 6
print(compras)



# Percorrendo um dicionário com um laço
for k, v in compras.items():
    print(f'O que vou comprar? {k} e a quantia? {v}')


# Percorrer apenas as chaves:
print("Na minha lista de compras, irei comprar apenas: ")
for k in compras.keys():
    print(f"{k}")


# Percorrer apenas os valores:
for v in compras.values():
    print(f"{v}")



# PREENCHENDO UM DICIONÁRIO COM INPUT
respostas = {}

votacao_ativa = True

while votacao_ativa:
    nome = input('Qual o seu nome? ').title()
    lugar = input('Diga um lugar que deseja visitar: ').title()
    
    respostas[nome] = lugar
    repetir = input('Outra pessoa deseja responder a enquete [S/N]? ').upper()

    if repetir == 'N':
        votacao_ativa = False

print('\n -- RESULTADOS -- ')
for k, v in respostas.items():
    print(f"{k} quer visitar {v}")