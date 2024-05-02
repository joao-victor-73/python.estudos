"""
                                        Calculadora Simples: 
Crie uma calculadora simples que permita ao usuário escolher entre operações de soma, 
subtração, multiplicação e divisão. Cada operação deve ser implementada como uma função separada.
"""


def soma(n1, n2):
    resultado = n1 + n2
    print(f"A Soma entre os numeros {n1} + {n2} resultou em {resultado}")


def subtracao(n1, n2):
    resultado = n1 - n2
    print(f"A subtração entre os numeros {n1} - {n2} resultou em {resultado}")


def multiplicacao(n1, n2):
    resultado = n1 * n2
    print(f"A multiplicação entre os numeros {
          n1} * {n2} resultou em {resultado}")


def divisao(n1, n2):
    resultado = n1 / n2
    print(f"A divisão entre os numeros {n1} / {n2} resultou em {resultado}")


# Programa Principal
print("""CALCULADORA SIMPLES 
1 - SOMA (+)
2 - SUBTRAÇÃO (-)
3 - MULTIPLICAÇÃO (*)
4 - DIVISÃO (/)
5 - SAIR""")

opcao = int(input("Digite a opção desejada: "))

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))


if opcao == 1:
    soma(n1, n2)

elif opcao == 2:
    subtracao(n1, n2)

elif opcao == 3:
    multiplicacao(n1, n2)

elif opcao == 4:
    divisao(n1, n2)

else:
    print('saaindo da calculadora!')
