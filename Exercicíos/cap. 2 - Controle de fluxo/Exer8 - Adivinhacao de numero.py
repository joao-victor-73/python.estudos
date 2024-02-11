"""
Exercício 8: Adivinhação de Número
Gere aleatoriamente um número entre 1 e 100. Peça ao usuário para adivinhar o número. 
Forneça dicas se o palpite foi muito alto ou muito baixo, até que o usuário acerte.
"""

import random
print("=" * 40)
print("         > ADIVINHAÇÃO DE NÚMERO <")
print("=" * 40)


num_random = random.randint(1, 101)

print("Eu gerei um número de 1 a 100 aleátoriamente, tente adivinhar qual é")

while True:
    adivinha = int(input("Qual número eu escolhi? "))

    if adivinha > num_random:
        print(f"O seu número, {adivinha}, é alto. Tente um mais baixo\n")
        continue
    elif adivinha < num_random:
        print(f"O seu número, {adivinha}, é baixo. Tente um mais alto\n")
        continue
    elif adivinha == num_random:
        print(
            f"O número digitado foi {adivinha} e é igual ao que eu escolhi: {num_random}")
        print("Parabéns. Você acertou!")
        break
