import datetime
import tkinter as tk
from PIL import Image, ImageTk


class Pessoa():
    def __init__(self, nome, aniversario):
        self.nome = nome
        self.aniversario = aniversario

    def idade(self):
        dia_atual = datetime.date.today()
        idade = dia_atual - self.aniversario.ano
        return idade


def getInput():
    nome = nomeEntry.get()
    macaco = Pessoa(nome, datetime.date(int(anoEntry.get()),
                                        int(mesEntry.get()),
                                        int(diaEntry.get())))

    textoArea = tk.Text(master=window, height=10, width=25)
    textoArea.grid(column=1, row=6)
    pergunta = f'Olá {macaco}! Sua idade é de {macaco.idade()} anos.'

    textoArea.insert(tk.END, pergunta)
    botao = tk.Button(window, text='Calcular Idade',
                      command=getInput, bg='pink')
    botao.grid(column=1, row=5)


window = tk.Tk()
window.geometry('380x480')
window.title('Calculadora de Idade')

nome = tk.Label(text='Nome')
nome.grid(column=0, row=1)

ano = tk.Label(text='Ano')
ano.grid(column=0, row=2)

mes = tk.Label(text='Mês')
mes.grid(column=0, row=3)

dia = tk.Label(text='Dia')
dia.grid(column=0, row=4)

nomeEntry = tk.Entry()
nomeEntry.grid(column=1, row=1)

anoEntry = tk.Entry()
anoEntry.grid(column=1, row=2)

mesEntry = tk.Entry()
mesEntry.grid(column=1, row=3)

diaEntry = tk.Entry()
diaEntry.grid(column=1, row=4)


imagem = Image.open('.\\Projetos\\calculadora_idade\\idade_foto.png')
imagem.thumbnail((300, 300), Image.ANTIALIAS)
foto = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(image=foto)
label_imagem.grid(column=1, row=0)


# Looping para gerar a janela.
window.mainloop()

'''< Problema atual(21/04/2023): O botão para calcular a idade não funciona. Resolver isso >'''
