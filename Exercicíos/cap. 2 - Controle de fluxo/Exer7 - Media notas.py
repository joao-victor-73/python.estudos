"""
Exercício 7: Média de Notas
Peça ao usuário para inserir notas de alunos (em uma escala de 0 a 10) até que ele decida parar.
Calcule e imprima a média das notas.
"""

print("=" * 40)
print("         > SOMA MÉDIA DE NOTAS <")
print("=" * 40)

soma_media = 0

nome = input("Olá. Qual o nome do aluno? ").capitalize()

while True:
    print("\nUtilizamos uma escala de 0 a 10 para as médias, digite apenas valores inteiros!\n")
    nota = int(input("Digite a nota: "))

    if nota > 10 or nota < 0:
        print("Média invalida! Digite um valor entre 0 ou 10")
        continue

    opcao = input("Deseja colocar outra média [S/N]? ").upper().strip()

    soma_media += nota

    if opcao == 'S':
        continue

    else:
        break

print(f"A soma de todas as médias do(a) aluno(a) {nome} é de {soma_media}")
