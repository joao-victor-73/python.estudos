import tkinter as tk
import random


def escolha_computador():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    return random.choice(opcoes)


def verificar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate!"
    elif (
        (escolha_usuario == "Pedra" and escolha_computador == "Tesoura")
        or (escolha_usuario == "Papel" and escolha_computador == "Pedra")
        or (escolha_usuario == "Tesoura" and escolha_computador == "Papel")
    ):
        return "Você ganhou!"

    else:
        return "O Computador ganhou!"


def jogar():
    escolha_usuario = opcao_var.get()
    if escolha_usuario:
        escolha_comp = escolha_computador()
        resultado = verificar_vencedor(escolha_usuario, escolha_comp)
        resultado_label.config(
            text=f"Computador Escolheu: {escolha_comp}\n{resultado}")
    else:
        resultado_label.config(text="Por favor, escolha uma opção!")


janela = tk.Tk()
janela.title("Pedro, Papel, Tesoura")

opcao_var = tk.StringVar()

instrucao_label = tk.Label(janela, text="Escolha uma opção: ")
instrucao_label.pack()

opcoes = ["Pedra", "Papel", "Tesoura"]
for opcao in opcoes:
    botao = tk.Radiobutton(janela, text=opcao, variable=opcao_var, value=opcao)
    botao.pack()

jogar_botao = tk.Button(janela, text="Jogar", command=jogar)
jogar_botao.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

opcao_var.set(None)
janela.mainloop()
