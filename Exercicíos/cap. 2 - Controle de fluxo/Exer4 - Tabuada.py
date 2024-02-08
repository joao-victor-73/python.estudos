"""
Exercício 4: Tabuada
Solicite ao usuário um número e imprima a tabuada desse número, do 1 ao 10
"""
print("=" * 30)
print("         > TABUADA! <")
print("=" * 30)

num = int(input("Digite um número para a tabuada: "))

if num > 0:
    for i in range(1, 11):
        print(f"{num} X {i} = {i * num}")

else:
    print("Digite um número positivo ou maior que 0")
