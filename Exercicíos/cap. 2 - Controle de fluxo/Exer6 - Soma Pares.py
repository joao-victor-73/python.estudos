"""
Exercício 6: Soma dos Números Pares
Solicite um número ao usuário e imprima a soma de todos os números pares de 1 até esse número.
"""

print("=" * 40)
print("         > SOMA NÚMEROS PARES <")
print("=" * 40)

num = int(input("Digite um número: "))
soma_pares = 0

for i in range(num, -1, -1):
    if i % 2 == 0:
        soma_pares += i

print(f"A soma de todos os números pares do número {num} até 1 é: {soma_pares}")
