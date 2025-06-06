""" 07/05/2025
Desafio 03: Crie uma função chamada eh_palindromo que receba uma string
            e verifique se ela é um palíndromo — ou seja, se pode ser lida 
            da mesma forma de trás para frente.

Exemplos:
            eh_palindromo("radar")         # deve retornar True
            eh_palindromo("Python")        # deve retornar False
            eh_palindromo("Ame a ema")     # deve retornar True

Regras:
            -> Ignore espaços e diferencie letras maiúsculas/minúsculas 
                (ou seja, trate tudo como minúsculo).

            -> Pode usar replace(" ", "") e .lower() para ajudar.

            -> Retorne True ou False.

"""


palavra_digitada = str(input("Digite uma palavra: ").lower().strip())

def eh_palindromo(palavra):

    if palavra ==  palavra[::-1]:
        print(f"A palavra digitada foi {palavra} e ela é um palindromo")
        return True

    else:
        print(f"A palavra digitada foi {palavra} e ela não é um palindromo")
        return False
    

eh_palindromo(palavra_digitada)