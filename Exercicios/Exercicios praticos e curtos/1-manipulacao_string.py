"""
- Crie uma função que analisa um texto e retorna:

    - Quantas palavras têm no texto
    - Quantas vezes cada vogal aparece
    - A palavra mais longa
"""


txt = input("Digite uma frase: ")
count = 0
vogal = 0

for p in txt.split():
    count += 1


for v in txt.upper():
    if v == 'A':
        vogal += 1
    elif v == 'E':
        vogal += 1
    elif v == 'I':
        vogal += 1
    elif v == 'O':
        vogal += 1
    elif v == 'U':
        vogal += 1

palavra_longa = ""
for l in txt.split():
    
    if len(l) > len(palavra_longa):
        palavra_longa = l



print(f"Quant. de palavras: {count}")
print(f"Quant. de vogais: {vogal}")
print(f"A palavra mais longa é: {palavra_longa}")
