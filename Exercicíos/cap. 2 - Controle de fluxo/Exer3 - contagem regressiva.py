"""
Exercício 3: Contagem Regressiva
Crie um programa que solicita ao usuário um número e, em seguida, imprime uma contagem regressiva até zero.
"""

print("=" * 30)
print("         > CONTADOR <")
print("=" * 30)

num = int(input("\nDigite um número: "))

if num > 0:
    print(f"\nO número digitado foi {num}. \n\nVamos contar até zero:")
    for i in range(num, -1, -1):
        print(i)

elif num == 0:
    print("O número digitado foi 0, tente digitar outro número")

else:
    print("O número é menor que zero, tente digitar um número positivo!")


""" VERSÃO COM WHILE
num = int(input("\nDigite um número: "))

if num > 0:
    while >= 0:
        print(num)
        num -= 1

elif num == 0:
    print("O número digitado foi 0, tente digitar outro número")

else:
    print("O número é menor que zero, tente digitar um número positivo!")


print("Contagem regressiva concluída!")
"""