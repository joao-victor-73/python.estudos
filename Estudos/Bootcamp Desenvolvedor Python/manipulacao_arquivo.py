# Aula 8.1 - Criação, Abertura e Fechamento de Arquivos

'''                     << DIFERENTES MODOS DE USO PARA UM ARQVIVO: >>
'r' - Modo somente leitura (modo padrão);
'w' - Modo de escrita. Cria um arquivo, caaso ainda não exista, ou substítui o arquivo atual;
'x' - Modo de escrita. Cria um arquivo e, se o arquivo já existir, retorna um erro.
'a' - Modo de escrita. Cria um arquivo, caso ainda não exista e adiciona dados ao final dele.
't' - Abre o arquivo no modo texto (modo padrão);
'b' - Abre o arquivo no modo binário.
'''

CAMINHO_ARQUIVO = ".\\teste_texto.txt"

# Lendo Todas as linhas de um arquivo e colocando elas dentro de uma variável de lista
with open(CAMINHO_ARQUIVO, 'r') as arq:
    linhas = arq.readlines()

    for i in linhas:  # Esse FOR vai mostrar linha por linha na tela
        print(i)
