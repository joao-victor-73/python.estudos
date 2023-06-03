# Aula: Manipulando Arquivos TXT em Python com a Expressão WITH

'''< Com a expressão WITH o método close() é executado automaticamente, sem necessidade de chama-lo >'''

texto = "Isso é um texto que diz uma frase que vai fazer sentido em algum momento. \n"
texto = texto + "Vamos colocar essa frase concatenada com a anterior. \n"
texto += "E é claro, devemos adicionar uma linha final. -----------------"

with open('.\\texto3.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(len(conteudo))
print(conteudo)

with open('.\\texto3.txt', 'w') as arquivo:
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[28:66])

arquivo = open('.\\texto3.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)
