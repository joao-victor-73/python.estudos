""""08/05/2025
Desafio 04: <Contador de frequência de letras>
            Crie uma função chamada frequencia_letras que receba uma frase e retorne um 
            dicionário com a frequência de cada letra presente nela. 

Exemplo:
            frequencia_letras("banana")  # Saída esperada: {'b': 1, 'a': 3, 'n': 2}

Regras:
            -> Ignore espaços e transforme todas as letras em minúsculas.

            -> Não conte números ou símbolos, apenas letras de A-Z.

            -> Use dict para armazenar as frequências.
"""

palavra = "banana"

def frequencia_letras(palavra):
    contagem_letras = {} # declarar a variável dentro da função para que ela seja independente e reutilizável.
    
    for l in palavra.lower().strip():
        if 'a' <= l <= 'z':
            if l in contagem_letras:
                contagem_letras[l] += 1
            else:
                contagem_letras[l] = 1
    
    return contagem_letras

print(frequencia_letras(palavra))