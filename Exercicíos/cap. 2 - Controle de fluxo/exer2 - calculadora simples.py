"""
Exercício 2: Calculadora Simples
Crie uma calculadora simples que solicita dois números e uma operação (+, -, *, /) ao usuário. 
Realize a operação e imprima o resultado.
"""
print("=" * 40)
print("         > CALCULADORA SIMPLES <")
print("=" * 40)

while True:
    print("Seja bem vindo a uma calculadora bem simples! \n")

    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    print("\n Agora vamos para as operações, escolha um abaixo por favor:\n")
    operacao = int(input(
        "1 - Adição (+) \n2 - Subtração (-) \n3 - Multiplicação (*) \n4 - Dvisão (/) \n >> Qual escolhe? "))

    print("")

    if operacao == 1:
        resultado = num1 + num2
        print(
            f"A soma entre os número {num1} + {num2} resultou em {resultado}")
        break

    elif operacao == 2:
        resultado = num1 - num2
        print(
            f"A subtração entre os número {num1} - {num2} resultou em {resultado}")
        break

    elif operacao == 3:
        resultado = num1 * num2
        print(
            f"A multiplicação entre os número {num1} * {num2} resultou em {resultado}")
        break

    elif operacao == 4:
        resultado = num1 / num2
        print(
            f"A divisão entre os número {num1} / {num2} resultou em {resultado:.2f}")
        break

    else:
        print("Opção não entendida, tente novamente!")
        continue
