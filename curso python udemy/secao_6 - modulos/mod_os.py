import os



# Ex2 - Verificando se um caminho existe:
caminho2 = os.path.join('arquivos', 'projetos', 'proc')
print(os.path.exists(caminho2))
# Retornará False ou True. Nesse caso o caminho não existe


# Ex1 - Criando um caminho
caminho = os.path.join('Python', 'secao_6 - modulos', 'teste.txt')
print(caminho)  # Python\secao_6 - modulos\teste.txt