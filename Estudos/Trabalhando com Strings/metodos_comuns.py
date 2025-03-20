"""
Um método em Python é uma função que pertence a uma classe ou a um objeto.
"""

frase = "A ajuda que você me forceu, foi util"
frase2 = "Será que aqui tem um numer0?"
palavra = "Games"
palavra2 = "12345"

# Método len() - mostra o tamanho da string.
print(len(frase))  # 36

# Método upper() - retorna uma string com todas maiusculas
print(frase.upper())  # A AJUDA QUE VOCÊ ME FORCEU, FOI UTIL

# Método lower() - retorna uma string com todas minusculas
print(frase.lower())  # a ajuda que você me forceu, foi util


# Método isalpha() - retorna "True" se todos os caracteres na string forem alfabetos, se não, retorna "False"
print(frase.isalpha())  # False
print(frase2.isalpha())  # False
print(palavra.isalpha())  # True
# Esse método também leva em conta os espaços em branco, ou seja,
# caso se tenha um espaço entre uma palavra e outra, ele considerará como um não alfabeto

# Método isnumeric() - retorna "True" se todos os caracteres da string forem numéricos, se não, retorna "False"
print(palavra.isnumeric())  # False
print(palavra2.isnumeric())  # True


# Método strip() - é usado para encontrar espaços em branco dos lados direito e esquerdo de uma string.
frase3 = "=|> Stardew Valley <|="
print(frase3)
print(f'{frase3.strip()}')


# Método join() - é usado para especificar os elementos de uma sequencia de caracteres para gerar uma nova
#                 sequencia de conexão.

frase4 = "09890988"  # 0-9-8-9-0-9-8-8
print('-'.join(frase4))


# Método Split() - ele permite dividir o conteúdo da variável de acordo com as condições especificadas
#                  em cada parâmentro da função; (E transforma elas em uma lista)

print(frase.split())
# ['A', 'ajuda', 'que', 'você', 'me', 'forceu,', 'foi', 'util']


# Método count() - retorna o número de ocorrências de uma substring na string fornecida.

print(frase.count('r'))  # vai contar quantos 'r' tem na frase (1)
print(frase.count('u'))  # vai contar quantos 'u' tem na frase (4)


# Método replace() - recebe dois argumentos, para fazer a localização e substituir valores dentro de uma string.
print(frase2.replace('i', '1'))  # Será que aqu1 tem um numer0?
print(frase2.replace('0', '0.0'))  # Será que aqui tem um numer0.0?
