"""
O fatiamento consiste em obter uma sub-string de uma determinada string, 
dividindo-a respectivamente do início ao fim. 
Selecionar uma fatia é como selecionar um caractere.
"""

frase = "Vamos jogar A Way Out juntos?"

print(len(frase))  # 29
print(frase[5:])  # jogar A Way Out juntos?
print(frase[0:20])  # Vamos jogar A Way Ou
print(frase[0:1])  # V
print(frase[-5:])  # ntos?


for f in frase[0:5]:
    print(f.title())
# V
# A
# M
# O
# S
