"""
Exercício 1: Verificação de número Par ou Ímpar
Peça ao usuário para inserir um número e imprima se é par ou ímpar.
"""
print("=" * 30)
print("   > Jogo do Par ou Impar <")
print("=" * 30)

num = int(input("Digite um número: "))

print(f"Verificando se o número: {num} é PAR ou IMPAR....\n")

if num % 2 == 0:
    print(f"O número {num} é PAR")
else:
    print(f"O número {num} é IMPAR")
