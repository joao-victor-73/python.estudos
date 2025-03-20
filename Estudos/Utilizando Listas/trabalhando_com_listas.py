frutas = ['Uva', 'Goiaba', 'Maça', 'Banana', 'Abacaxi', 'Laranja']

# loops for com listas
for f in frutas:
    print(f)
# Uva
# Goiaba
# Maça
# Banana
# Abacaxi
# Laranja


for f in frutas:
    if f == 'Goiaba':
        print(f"Não precisamos de {f}")


for i in range(len(frutas)):
    print(f'{i+1} - {frutas[i]}')
#1 - Uva
#2 - Goiaba
#3 - Maça
#4 - Banana
#5 - Abacaxi
#6 - Laranja

